
import os
import time
import numpy as np
import logging
from sklearn.metrics.pairwise import cosine_similarity
from src.provider.models.face_detect.model import RetinaFace
from src.provider.models.face_embedding.model import ArcFace
from src.utils.read_image import read_image, read_img_from_bytes


logger = logging.getLogger('AI_Service')


class Agent():
    def __init__(self,detection_score=0.4):
        
        self.face_detect_gpuid = -1
        self.face_embedding_gpuid = -1
      
        self.__setup_model(detection_score)

    def __setup_model(self,detection_score):
        model_path = os.path.join('src','provider','models')
        logger.info(
            'Deploy face detector model on device: ' + str(self.face_detect_gpuid))
        self.face_detector = RetinaFace(os.path.join(model_path, 'face_detect/data/mnet.25'), 0, self.face_detect_gpuid,
                                            'net3')
        self.detection_score = detection_score

        logger.info(
            'Deploy face embedded model on device: ' + str(self.face_embedding_gpuid))
        self.face_embedding = ArcFace(os.path.join(model_path, 'face_embedding/data/resnet50/model'),
                                        self.face_embedding_gpuid,
                                        image_size=(112, 112))


    def __read_img(self, img_byte1, img_byte2):
        img_dict = {}
        img_dict['img1'] = read_img_from_bytes(img_byte1)
        img_dict['img2'] = read_img_from_bytes(img_byte2)
        return img_dict

    def __face_verify(self,img_obj):

        embeddings_dict = {}
        img_dict = self.__read_img(
            img_obj.img1, 
            img_obj.img2
            )

        for idx, key in enumerate(img_dict):

            min_width = 0
            largest_bbox = None
            largest_landmarks = None
            t0_all = time.time()

            # Face detection
            t0 = time.time()
            bboxes, landmarks = self.face_detector.detect(img_dict[key], threshold=self.detection_score)
            t1 = time.time()
            logger.info("detected {0}: {1} ms".format(idx,(t1-t0)*1000))
            # filter biggest face    
            for bbox, landmark in zip(bboxes, landmarks):
                box_width = bbox[2] - bbox[0]
                if box_width > min_width:
                    min_width = box_width
                    largest_bbox = bbox
                    largest_landmarks = landmark

            largest_bbox = np.int0(largest_bbox) # Round values in array

            # Face alignment and preprocess
            face = self.face_embedding.image_preprocess(
                img_dict[key], largest_bbox, largest_landmarks, image_size='112,112')

            # Face embeddimg
            t0 = time.time()
            embeddings = self.face_embedding.get_embedding(face)
            t1 = time.time()
            logger.info("embeded {0}: {1} ms".format(idx,(t1-t0)*1000))
            embeddings_dict[key] = [embeddings]

            t1_all = time.time()
            logger.info("all {0}: {1} ms".format(idx,(t1_all-t0_all)*1000))
        
        # compare face with cosine_similarity
        similarity_score = cosine_similarity(embeddings_dict['img1'], embeddings_dict['img2'])
        logger.info("img1: {0}, img2: {1}, similarity_score: {2}".format(img_obj.img1_name, img_obj.img2_name, similarity_score[0][0]))

        return similarity_score

    def run_verify(self, img_obj):
        '''
        Just compare 1:1 
        '''
        similarity_score = self.__face_verify(img_obj)

        return str(similarity_score[0][0])

