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
    model = await tf.loadGraphModel('http://127.0.0.1:8887/model3/model.json');
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

// ! predict the input image
async function predict(){
    // get the image element
    let img = document.getElementById('preview_img')
    // resize the image and adding extra dimension
    var raw = tf.browser.fromPixels(img);
	var resized = tf.image.resizeBilinear(raw, [WIDTH,HEIGHT]);
	var tensor = resized.expandDims(0);
    var prediction = model.predict(tensor);
    var pIndex = tf.argMax(prediction, 1).dataSync();
    var dictionary = {0:'0', 1:'1', 2 :'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A',
    11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K',
    21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T',
    30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'};
    alertText = dictionary[pIndex];
    alert(alertText);
}