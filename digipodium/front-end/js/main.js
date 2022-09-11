let btn= document.querySelector('.add');
let btn1= document.querySelector('.diff');
let btn2= document.querySelector('.prod');
let btn3= document.querySelector('.div');
let ans= document.querySelector('.answer');
btn.onclick= function(e){    // e stands for event but anything can be written
    e.preventDefault();
    var num1= document.querySelector('#num1').value;
    var num2= document.querySelector('#num2').value;
    ans.innerHTML= parseInt(num1)+parseInt(num2);
    alert(parseInt(num1)+parseInt(num2));
}



btn1.onclick= function(e){ 
    e.preventDefault();
    var num1= document.querySelector('#num1').value;
    var num2= document.querySelector('#num2').value;
    ans.innerHTML= parseInt(num1)-parseInt(num2);
    // alert(parseInt(num1)-parseInt(num2));
}


btn2.onclick= function(e){
    e.preventDefault();
    var num1= document.querySelector('#num1').value;
    var num2= document.querySelector('#num2').value;
    ans.innerHTML= parseInt(num1)*parseInt(num2);
    // alert(parseInt(num1)*parseInt(num2));
}

btn3.onclick= function(e){
    e.preventDefault();
    var num1= document.querySelector('#num1').value;
    var num2= document.querySelector('#num2').value;
    ans.innerHTML= parseInt(num1)/parseInt(num2);
    // alert(parseInt(num1)/parseInt(num2));
}