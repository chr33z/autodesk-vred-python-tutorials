import { api } from 'http://localhost:8888/api.js';
            
// Connect event listener (signal)
api.vrAnnotationService.annotationsAdded.connect(() => console.log('Annotations added'));

// Add an annotation with name and text to the scene
function addAnnotation(name, text) {
    api.vrAnnotationService.createAnnotation(name)
    .then(() => {
        api.vrAnnotationService.findAnnotation(name)
        .then(a => a.setText(text));
    })
    .catch(() => console.error('Add annotation failed'));
}

// Get a list of all annotations
function getAnnotations() {
    api.vrAnnotationService.getAnnotations()
    .then(annotations => annotations.forEach(a => console.log(a)))
    .catch(() => console.error('Get annotations failed')); 
}

// Add both functions to the global scope
// So that we can call them from the html document
window.addAnnotation = addAnnotation;
window.getAnnotations = getAnnotations;