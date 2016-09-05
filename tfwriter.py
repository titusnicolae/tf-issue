import tensorflow as tf


with tf.Session() as sess:
    record_writer = tf.python_io.TFRecordWriter("range.tfrecord")
    for i in range(10):
        example = tf.train.Example(
            features=tf.train.Features(feature={
                'int': tf.train.Feature(int64_list=tf.train.Int64List(value=[i])),
            }))
        record_writer.write(example.SerializeToString())
    record_writer.close()
