import tensorflow as tf
reader = tf.TFRecordReader()

filename_queue=tf.train.string_input_producer(["range.tfrecord"])

key, data = reader.read(filename_queue)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord = coord)
    for i in range(20):
        output = sess.run([key, data])
        print(i, output)
    
    coord.request_stop()
    coord.join(threads, stop_grace_period_secs=100)
