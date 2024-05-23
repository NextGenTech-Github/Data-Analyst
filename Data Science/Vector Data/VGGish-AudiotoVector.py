# pip install tensorflow vggish
import tensorflow as tf
import vggish_input
import vggish_params
import vggish_postprocess
import vggish_slim

def generate_audio_vector(audio_path):
    examples_batch = vggish_input.wavfile_to_examples(audio_path)
    with tf.Graph().as_default(), tf.Session() as sess:
        vggish_slim.define_vggish_slim(training=False)
        vggish_slim.load_vggish_slim_checkpoint(sess, 'vggish_model.ckpt')
        features_tensor = sess.graph.get_tensor_by_name(vggish_params.INPUT_TENSOR_NAME)
        embedding_tensor = sess.graph.get_tensor_by_name(vggish_params.OUTPUT_TENSOR_NAME)
        [embedding_batch] = sess.run([embedding_tensor], feed_dict={features_tensor: examples_batch})
        return embedding_batch

audio_path = "path_to_audio.wav"
audio_vector = generate_audio_vector(audio_path)
print(audio_vector)
