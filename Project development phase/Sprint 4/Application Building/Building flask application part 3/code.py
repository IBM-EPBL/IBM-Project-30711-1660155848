def detect(frame):
    vals = ['A','B','C','D','E','F','G','H','I']
    img = resize(frame,(64,64,1))
    img = np.expand_dims(img,axis=0)
    if(np.max(img) > 1):
        img = img/225.0
    with graph.as_default():
            prediction = model.predict_classes(img)
    print(prediction)
    pred=vals[predication[0]]
    print(pred)
    return pred




@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundry=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)