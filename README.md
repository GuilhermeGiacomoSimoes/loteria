# sugestão de número baseado em padrões reconhecidos

## Rodando o script
	* $ python3 loteria.py

	* Se vc baixar o csv desse repositório, vai ter quase toda a base de jogos da megasena, dependendo da frequencia da minha atualização.

	* Se estiver desatualizado, ou vc não quiser baixar esse csv, sem problemas, o script identifica isso e vai baixar do site da megasena toda a base, ou somente os jogos que faltam... tenha paciência, pois demora :/

	* Após a atualização, ou o download de toda a base, ele vai sugerir uma sequência de 6 dígitos :) 

## Padrões para a sequência de dezenas
	* É mais comum sair dezenas de 1 a 30 do que as de 31 a 60, então o script vai sugerir quatro dezenas de 1 a 30 e duas dezenas de 31 a 60;

	* Nas dezenas de 30 a 50, é comum aparecerem duas dezenas com intervalo pequeno (exatamente de 2 a 4) então duas das seis dezenas que forem sugeridas terão esse intervalo.

	* O mais importante de tudo é sugerir uma sequência de números que NUNCA foi sorteado, por motivos óbvios, então  o script vai sugerir uma dezena que nunca foi sorteada. 
