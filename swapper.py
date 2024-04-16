import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image


assert insightface.__version__>='0.7'

def swapper(input_path,output_path):
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)

    img = cv2.imread(input_path)
    faces_input = app.get(img)
    faces_input = sorted(faces_input, key = lambda x : x.bbox[0])
    assert len(faces_input)==1
    source_face = faces_input[0]
    res = cv2.imread(output_path)
    faces_output = app.get(res)
    faces_output = sorted(faces_output, key = lambda x : x.bbox[0])
    assert len(faces_output)==1
    face_output = faces_output[0]
    res = swapper.get(res, face_output, source_face, paste_back=True)
    return res

if __name__ == '__main__':
    swapper()