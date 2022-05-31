import { loadGraphModel } from "@tensorflow/tfjs";

const OBJ_DETECTION_MODEL_PATH =
  "machine_learning_model/license_plate_object_detection_model/model.json";

const CHARACTER_RECOGNITION_MODEL_PATH =
  "machine_learning_model/license_plate_object_detection_model/model.json";

  
export async function load_model() {
  // const model = await loadGraphModel("/web_model/model.json");
  const model = await loadGraphModel(OBJ_DETECTION_MODEL_PATH);
  return model;
}