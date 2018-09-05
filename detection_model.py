import os
import numpy as np
import operator
import tensorflow as tf
import settings
import time

class DetectionModel:
    def __init__(self, path_to_ckpt):
        # Code adapted from https://gist.github.com/madhawav/1546a4b99c8313f06c0b2d7d7b4a09e2
        self.path_to_ckpt = path_to_ckpt

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.path_to_ckpt, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.Session(graph=self.detection_graph)

        # Definite input and output Tensors for detection_graph
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')




    def predict(self, image):
        # Code adapted from https://gist.github.com/madhawav/1546a4b99c8313f06c0b2d7d7b4a09e2
        # Expand dimensions since the trained_model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # Actual detection.
        start_time = time.time()
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        end_time = time.time()

        print("Elapsed Time:", end_time-start_time)

        im_height, im_width,_ = image.shape

        
        ''' Commented out to return normalized coordinates instead
        # boxes_list = [None for i in range(boxes.shape[1])]
        # for i in range(boxes.shape[1]):
        #     boxes_list[i] = (int(boxes[0,i,0] * im_height),
        #                 int(boxes[0,i,1]*im_width),
        #                 int(boxes[0,i,2] * im_height),
        #                 int(boxes[0,i,3]*im_width))

        # return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])
        '''

        output_dict = {}
        output_dict['detection_boxes'] = boxes[0].tolist()
        output_dict['detection_scores'] = scores[0].tolist()
        output_dict['detection_classes'] =  [int(x) for x in classes[0].tolist()]
        output_dict['num_detections'] = int(num[0])

        return output_dict

    

    def __enter__(self):
        # for using with "with" block
        return self

    def __exit__(self, type_, value, traceback):
        # close session at the end of "with" block
        self.destroy()


    def destroy(self):
        '''
        Close TensorFlow session
        '''
        self.sess.close()
        self.default_graph.close()
