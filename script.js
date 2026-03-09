async function generateScript(){

const title = document.getElementById("title").value;
const genre = document.getElementById("genre").value;
const idea = document.getElementById("idea").value;
const characters = document.getElementById("characters").value;

const response = await fetch("http://127.0.0.1:5000/generate_script",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
title:title,
genre:genre,
idea:idea,
characters:characters
})

});

const data = await response.json();

document.getElementById("output").innerText =
"Title: "+data.title+
"\nGenre: "+data.genre+
"\nStory: "+data.idea+
"\n\nScenes:\n"+data.scenes.join("\n")+
"\n\nDialogues:\n"+data.dialogues.join("\n");

}