const mongoose = require("mongoose");

const imageSchema = new mongoose.Schema({
  filename: {
    type: String,
    required: true,
  },
  data: [],
});

module.exports = mongoose.model("Image", imageSchema);
