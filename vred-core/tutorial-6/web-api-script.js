import { api } from "http://localhost:8888/api.js";

// -- PART 1 --

// Add an annotation with a name and a description
function addAnnotation(name, description) {
  api.vrAnnotationService
    .createAnnotation(name)
    .then(() => {
      api.vrAnnotationService.findAnnotation(name).then((a) => {
        a.setText(description);
        addEventMessage("Annotations added successfully");
      });
    })
    .catch(() =>
      document.getElementById("python-response")("Add annotation failed")
    );
}

// Annotation form
annotationForm.onsubmit = (ev) => {
  ev.preventDefault();
  const name = ev.target.elements.name.value;
  const description = ev.target.elements.description.value;
  addAnnotation(name, description);
};

// -- END: PART 1 --

function addEventMessage(message) {
  var textarea = document.getElementById("python-response");
  var text = textarea.value;
  textarea.value = message + "\n" + text;
}

// Adds a new list item to the unordered list #annotations.
// function addAnnotationItem(name, description, deleteCallback) {
function addAnnotationItem(name, description) {
  let item = undefined;
  if (name) {
    item = document.createElement("li");
    const nameItem = document.createElement("strong");
    nameItem.appendChild(document.createTextNode(name));
    item.appendChild(nameItem);
  } else {
    return;
  }

  if (description) {
    const descriptionItem = document.createElement("span");
    descriptionItem.appendChild(document.createTextNode(description));
    item.appendChild(descriptionItem);
  }

  const link = document.createElement("a");
  link.href = `?delete=${name}`;
  link.appendChild(document.createTextNode("( X )"));
  link.onclick = (e) => {
    deleteAnnotation(name);
    e.preventDefault();
  };
  item.appendChild(link);

  document.getElementById("annotations").appendChild(item);
}

function deleteAnnotation(name) {
  api.vrAnnotationService
    .findAnnotation(name)
    .then((a) => api.vrAnnotationService.deleteAnnotation(a));
}

// Delete all annotations in the list
function deleteAnnotationItems() {
  const list = document.getElementById("annotations");
  list.textContent = "";
}

// -- PART 2.2 --

// Loads annotations and adds annotation names to the unordered list #annotations.
function loadAnnotations() {
  deleteAnnotationItems();

  api.vrAnnotationService
    .getAnnotations()
    .then((annotations) => {
      if (annotations.length > 0) {
        annotations.forEach(async (a) => {
          const name = await a.getName();
          const description = await a.getText();
          addAnnotationItem(name, description);
        });
      } else {
        addAnnotationItem("No annotations found.");
      }
    })
    .then(() => addEventMessage("Annotations loaded successfully"))
    .catch(() => addEventMessage("Loading annotations failed"));
}

// -- END: PART 2.2 --

// -- PART 2.1 --

// Add event listeners
api.vrAnnotationService.annotationsAdded.connect(() => {
  loadAnnotations();
});

api.vrAnnotationService.annotationsDeleted.connect(() => {
  loadAnnotations();
});

// Load annotations
loadAnnotations();

// -- END: PART 2.1 --
