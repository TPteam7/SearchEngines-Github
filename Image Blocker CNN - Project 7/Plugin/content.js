// const imgs = document.getElementsByTagName('img');
// for ( let i = 0; i < imgs.length; i++) {
//     imgs[i].src = 'https://media.licdn.com/dms/image/v2/D5603AQHPvFDtUSo3-A/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1669181171687?e=1738800000&v=beta&t=PU83cSQecZJPExgAwj7fq8aKhhcvS0L2MCowGHbsQYw';
// }

let model;

// Load the model
async function loadModel() {
  model = await tf.loadLayersModel(chrome.runtime.getURL('tfjs_model/model.json'));
  console.log("Model loaded!");
}
