let btnpaciente = document.getElementById('first');
let btnorganization = document.getElementById('second');
let container = document.getElementById('container');
let x = document.getElementById('paciente');
let y = document.getElementById('instituicao');
let a = document.getElementById('formulários');


btnpaciente.addEventListener('click', function(){
    a.style.display =  'block';
    container.style.display = 'none';
    x.style.display =  'block';
    y.style.display =  'none';
    console.log('clicou1');
});

btnorganization.addEventListener('click', function(){
    a.style.display = 'block';
    x.style.display =  'none';
    y.style.display =  'block';
    container.style.display = 'none';
    console.log('clicou2');
});



