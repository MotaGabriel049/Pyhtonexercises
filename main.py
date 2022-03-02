print('''
% % % % % % % % % % % % % % % % % % % % % % % % % %
   % % % % % % % % % % % % % % % % % % % % % % % % % %

        .       .    )        .           .
   .       *             .         .
                 .                      .
   .       .       .'          .
                  '.              *        .
      .   '        .'     .              .
              _.---._   .            .     *
    *       .'       '.
        _.-~===========~-._
       (___________________)       .   *
  __         \_______/       ______        __
    |                       |      |      |  |
    |                       |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~ jro    ~--.
                    /|\
                   /   \
                  /  |  \
                 /       \
   \|/          /    |    \
               /           \    "It's probably a HUNDRED
              /      |      \    MILES to a gas station!
             /               \   This wind is RUINING MY
            /        |        \   HAIR! Why I married a
           /                     FOOL like YOU, I'll NEVER
          /   ____   |           KNOW! My parents TOLD ME
         /   /  __)         ___   you were no good!..."
        /    \(~oo   |     (___)  /
       /     _\_-/_       (_o o_)
      /     /  \/  \ |    (_\O/_)   \
     /     / /    \ \     //\_/\\    \
    /      \ |    /_/    //(_ _)\\    \
   /        \|___(_/     \\/   \//     \    \|/
             |    \      (/_____\)
             | |\  \      / /| |
             | |/  /      \ \| |
             |_/__/        \_|_|
            (__[__)        <_<_>

  * * * * * * * * * * * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * * * * * * * * * *
''')
print("\tBem vindo ao Jogo 'Abduzidos'.\n")
print("Você e sua esposa estão viajando para casa dos pais dela e por algum motivo óbvio, a gasolina de vocês acabam e o carro para no meio da estrada, por azar acabaram dando de cara com um OVNI que abduziu sua esposa. Sua missão é encontrá-la no posto de gasolina mais perto!!.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

start = input("\tQuer começar a jogar?\n 'Sim' ou 'Nao' - " ).lower()
if (start == 'sim'):
  print('''
      .       .    )        .           .
   .       *             .         .
               .                      .
   .       .                   .
                                *        .
      .   '               .              .
              _.---._   .            .     *
    *       .'       '.
        _.-~===========~-._
       (___________________)       .   *
  __  .'     \_______/   .'  ______        __
    |              .'  .'   |      |      |  |
    |             '         |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~ jro    ~--.
                    /|\
                   /   \
                  /  |  \
                 /       \
   \|/          /    |    \
               /           \
              /      |      \
             /               \
            /
           /       "BRING MY WIFE BACK,
          /    __  YOU COSMIC KIDNAPPERS!"
         /    /  \ /
        /    (\__/)  |            \
       /     _\__/_                \
      /     /      \ |              \
     /     / /   / /                 \
           \ |   \_\                  \
            \|____\_)                  \    \|/
             |    \
             | |\  \
             | |/  /
             |_/__/
            (__[__)''')
  print("\nVocê tem dois caminhos, seguir em frente em uma estrada longa ou virar a direita e pegar um atalho...\n")

  escolha1 = input("Qual você escolhe -'Frente' ou 'Direita'?\n").lower()


  if(escolha1 == 'frente'):
  
   escolha2 = input("\nVocê consegue enxergar 2 luzes em sua frente uma vermelha e outra azul...\n Qual luz você deseja seguir? - 'Vermelha' ou 'Azul':").lower()
   if(escolha2 == 'azul'):
    escolha3 = input("\nVocê se aproxima da luz azul e percebe que na verdade tem 3 estações de posto de gasolina...\n Para qual você quer ir? - 'Amarelo', 'Laranja' ou 'Verde' ").lower()
    if(escolha3 == 'amarelo'):
     print("\nVocê chega no posto e percebe que é uma armadilha. Ao sair correndo você acaba pisando em falso em um buraco...\n GAME OVER!!!'")
    elif(escolha3 == 'laranja'):
     print("\nVocê encontrou sua esposa e conseguiu pegar gasolina para o carro! Sua esposa te ama como nunca!! \n YOU WIN!!!'")  
    elif(escolha3 == 'verde'):
     print("\nVocê foi parar no posto errado e acaba sendo abduzido no lugar da sua esposa, agora ela pode ter uma vida feliz...\n GAME OVER!!!'")
     
   elif(escolha2 == 'vermelha'):
    print("\nVocê se aproxima da luz vermelha e observa que na verdade é a luz de um bar, então você percebe que está muito longe do posto e decide ficar por lá mesmo para 'Esquecer' sua esposa, afinal, ela nem te amava tanto assim...\n GAME OVER!!!")
  elif(escolha1 == 'direita'):
   print("\nVocê escolheu pegar um atalho e acabou dando de cara com hienas cheias de fome.\n Game Over!")
elif(start == "nao"):
    print("\nTudo bem, volte mais tarde! :-)")