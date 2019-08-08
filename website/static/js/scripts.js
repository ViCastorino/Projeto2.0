
let btnpaciente = document.getElementById('first');
let btnorganization = document.getElementById('second');
let a = document.getElementById('maior');
let treze = document.getElementById('treze');
let p = document.getElementById('5');
let x = document.getElementById('form.a');
let y = document.getElementById('form.b');

btnpaciente.addEventListener('click', function(){
    a.style.display =  'block';
    treze.style.display = 'none';
    x.style.display =  'block';
    y.style.display =  'none';
    // p.style.display =  'none';
    console.log('clicou1');
});

btnorganization.addEventListener('click', function(){
    a.style.display = 'block';
    x.style.display =  'none';
    y.style.display =  'block';
    
    // p.style.display =  'none';
    treze.style.display = 'none';
    console.log('clicou2');
});


// function inicaLogin(loginID) {
//     const login = document.getElementById(loginID);
//     login.classList.add('mostrar');
// }
// const entre =document.querySelector('.secondary');
// entre.addEventListener('click',function(){
//     inicaLogin('login');
// } );
