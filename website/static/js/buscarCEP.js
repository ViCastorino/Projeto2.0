(function(){
let inputCEP = document.querySelector(".cep-input");
let btn = document.querySelector(".btn");

// Ao pressionar uma tecla nesses campos, aplicar as funções para formata-los, adicionando . e - nos devidos lugares
inputCEP.onkeyup = mascaraCEP;


btn.onclick = function () {
 renderEndereco(inputCEP.value);
}

function mascaraCEP() {
 /* 
 O replace é uma método de string que substitui o primeiro parâmetro pelo segundo.  
 /\D/g que é uma expressão regular que seleciona tudo que não for um valor numérico 
 Veja mais aqui https://regex101.com/r/9iNvjU/2 e aqui 
 E vai substituir por um nada '', ou seja, o usuário não vai conseguir digitar texto nesse campo
 */
 inputCEP.value = inputCEP.value.replace(/\D/g, "");

 //Depois de pegar um valor numérico 5x, adiciona um traço nessa string 
 inputCEP.value = inputCEP.value.replace(/(\d{5})/, "$1" + "-");
}

function renderEndereco($cep){
 $cep.replace(/\D/g, "");

 /* 
 Ajax é um jeito de pegar documentos vindos de outros sites, 
 geralmente é retornado um JSON tipo assim https://viacep.com.br/ws/01001000/json/ 
 */
 const ajax = new XMLHttpRequest();
 const url = `https://viacep.com.br/ws/${$cep}/json/`;

 ajax.open("GET", url, true);
 ajax.send(null);

 /* Se a requisição for ok, e nosso script conseguiu pegar esse documento,
    que será o ajax.responseText, transformar ele no objeto endereco, 
    e colocar cada um de seus atributos em campos diferentes 
 */
 ajax.onreadystatechange = _ => {
  if (ajax.readyState == 4) {
   let endereco = JSON.parse(ajax.responseText);
   return (
    document.querySelector('[name="rua"]').value = endereco.logradouro,
    document.querySelector('[name="complemento"]').value = endereco.complemento,
    document.querySelector('[name="bairro"]').value = endereco.bairro,
    document.querySelector('[name="municipio"]').value = endereco.localidade,
    document.querySelector('[name="uf"]').value = endereco.uf
   )
  }
 };
}
})()