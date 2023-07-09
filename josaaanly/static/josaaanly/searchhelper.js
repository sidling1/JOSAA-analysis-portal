console.log('Hello World')
document.body.addEventListener('keypress',()=>checkdata())


function checkdata(){
    
    data = document.getElementsByTagName('form')
    pattern = document.getElementById('pattern').value

    var regex = new RegExp(pattern.toUpperCase())

    var n = data.length

    for(i=0;i<n;i++){
        if(regex.test(data[i].id.toUpperCase())){
            data[i].style.display = 'block'
        }else{
            data[i].style.display = 'none'
        }
    }
}