(function () {
 let inputCPF = document.querySelector(".cpf-input");
 // Ao pressionar uma tecla nesse input, aplicar as funções para formata-los, adicionando . e - nos devidos lugares
 inputCPF.onkeyup = mascaraCPF;

 function mascaraCPF() {
 /* 
 O replace é uma método de string que substitui o primeiro parâmetro pelo segundo.  
 /\D/g que é uma expressão regular que seleciona tudo que não for um valor numérico 
 Veja mais aqui https://regex101.com/r/9iNvjU/2  
 Aqui ele vai substituir por um nada '', ou seja, o usuário não vai conseguir digitar texto nesse campo
 */
  inputCPF.value = inputCPF.value.replace(/\D/g, "");

  // A cada 3 valores numéricos digitados, adiciona um ponto na string
  inputCPF.value = inputCPF.value.replace(/(\d{3})/, "$1" + ".");
  inputCPF.value = inputCPF.value.replace(/\.(\d{3})/, ".$1" + ".");
  inputCPF.value = inputCPF.value.replace(/\.(\d{3})(\d{2})/, ".$1-$2");
 }

})()