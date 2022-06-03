// JavaScript Code

// ! constants
const WIDTH = 75;
const HEIGHT = 100;

// variables
let uploadImage = document.querySelector('input');
let preview = document.querySelector('.preview');
let predictBtn  = document.querySelector('.inference-btn')
let predictResult = document.querySelector('.inference-result')

// ! adding event listener if the file 
uploadImage.addEventListener('change', updateImagePreview);
predictBtn.addEventListener('click', predict);

// create async function for model initialization
async function initializeModel(){
    model = await tf.loadGraphModel('http://127.0.0.1:8887/model2/model.json');
}
// initialize model immediately
initializeModel();

// ! function for updating image preview after file is submitted
function updateImagePreview(){
    console.log('masuk')
    let files = uploadImage.files
    if (files.length === 0){
        console.log('file is empty')
    }
    else{
        preview.innerHTML = ''
        let img = document.createElement('img');
        for (let file of files){
            img.src = URL.createObjectURL(file);
            img.width = 50
            img.id = 'preview_img'
            preview.appendChild(img)
        }
    }
}
      
function onOpenCvReady() {
}

// ! predict the input image
async function predict(){
    // get the image element
    let img2 = document.getElementById('preview_img')
    let img = cv.imread(img2)
    let size =  img.size();
    cv.cvtColor(img, img, cv.COLOR_BGR2GRAY);
    cv.bitwise_not(img, img);
    cv.adaptiveThreshold(img, img, 255,
	cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 43, 9);
    // resize the image and adding extra dimension
    let tensorImg = tf.browser.fromPixels(img).resizeNearestNeighbor([WIDTH, HEIGHT])//.toFloat().expandDims();
    const div_canvas = document.getElementById('canvas')
    const canvas = document.createElement('canvas');
    canvas.width = tensorImg.shape.width
    canvas.height = tensorImg.shape.height
    await tf.browser.toPixels(tensorImg, canvas);
    div_canvas.appendChild(canvas)
    console.log(tensorImg.shape)
    // normalize the image pixel values
    //let normTensorImg = tensorImg.div(255);
    // let prediction = await model.predict(tensorImg).array();
    // let alertText = '';
    // var dictionary = {0:'0', 1:'1', 2 :'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A',
    // 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K',
    // 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T',
    // 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'};
    // console.log(prediction[0])
    // var res = tf.argMax(prediction[0]).print();
    // console.log(res);
    // alertText = dictionary[res];
    // // if (prediction[0] <= 0.1) {
    // //     alertText = `Cat with ${((1-prediction[0]) * 100)}% confidence`;
    // // } else if (prediction[0] >= 0.9) {
    // //     alertText = `Dog with ${(prediction[0] * 100)}% confidence`;
    // // } else {
    // //     alertText = "This is Something else";
    // // }
    // alert(alertText);
}