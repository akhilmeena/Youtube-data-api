function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function SumOfNumbers() {
  document.getElementById("SumExam").innerHTML = 2+5;
}

function goPython(){
  $.ajax({
  url: "/scripts/file.py",
  context: document.body
  }).done(function() {
    alert('finished python script');;
  });
}

//alert("delivering hearts to my followers..❣️");
alert("loading animation... plz wait.");