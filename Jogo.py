import tkinter
from tkinter import *
from tkinter import ttk

# cores

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando janela

janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

#Dividindo a janela
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#Configuração frame_cima
app_x = Label(frame_cima, text='X', height=1, relief="flat", anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text='Jogador 1', height=1, relief="flat", anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text='0', height=1, relief="flat", anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_pontos = Label(frame_cima, text='x', height=1, relief="flat", anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co0)
app_pontos.place(x=108, y=25)

app_o= Label(frame_cima, text='O', height=1, relief="flat", anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)

app_o = Label(frame_cima, text='Jogador 2', height=1, relief="flat", anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)

app_o_pontos = Label(frame_cima, text='0', height=1, relief="flat", anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)

#Lógica

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

jogando = 'X'
contador = 0

def iniciar_jogo():
    #Controlar o jogo
    def control(i):
        global jogando
        global contador
        jogou = 0
        
        #Compara o valor recebido
        if i == str(1):
            
            #verifica se a posição esta vazia
            if b_0['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
                
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(2):
            
            #verifica se a posição esta vazia
            if b_1['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(3):
            
            #verifica se a posição esta vazia
            if b_2['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(4):
            
            #verifica se a posição esta vazia
            if b_3['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(5):
            
            #verifica se a posição esta vazia
            if b_4['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(6):
            
            #verifica se a posição esta vazia
            if b_5['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(7):
            
            #verifica se a posição esta vazia
            if b_6['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(8):
            
            #verifica se a posição esta vazia
            if b_7['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
        if i == str(9):
            
            #verifica se a posição esta vazia
            if b_8['text']=='':
                
                #verifica quem esta jogando
                if jogando == 'X':
                    cor = co7
                    
                if jogando == 'O':
                    cor = co8
                    
                #Marcando a posição
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
                
                
                    
                #incrementa o contador
                contador += 1
                
                #Verificação se houve ação no jogo
                jogou =1
                
                #Após o contador atingir o valor 5 ele verifica se há ganhador
        if contador >=5:
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                winner(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                winner(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                winner(jogando)
            elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                winner(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                winner(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                winner(jogando)
            elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                winner(jogando)
            elif tabela[2][0] == tabela[1][1] == tabela[2][0] != "":
                winner(jogando)
            elif contador >= 9:
                winner('empate')
                
        #troca o jogador
        if jogou == 1:
            if jogando == 'X':
                jogando = 'O'
                        
            else:
                jogando = 'X'
                    
    
    #Decide o vencedor
    def winner(win):
        global contador
        global score_1
        global score_2
        
        #zera o contador
        contador = 0
        
        #Limpa o jogo
        b_0['text']=''
        b_1['text']=''
        b_2['text']=''
        b_3['text']=''
        b_4['text']=''
        b_5['text']=''
        b_6['text']=''
        b_7['text']=''
        b_8['text']=''
        
        #Disabilita os botôes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        
        if win == 'X':
            score_1 += 1
            app_vencedor= Label(frame_baixo, text='Jogador 1 Venceu', width=17, relief="flat", anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
            app_vencedor.place(x=40, y=90)
            app_x_pontos['text'] = score_1
            
        elif win == 'O':
            score_2 += 1
            app_vencedor= Label(frame_baixo, text='Jogador 2 Venceu', width=17, relief="flat", anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
            app_vencedor.place(x=40, y=90)
            app_o_pontos['text'] = score_2
            
        else:
            app_vencedor= Label(frame_baixo, text='Empate', width=17, relief="flat", anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
            app_vencedor.place(x=40, y=90)
            
        def start():
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            app_vencedor.destroy()
            b_jogar.destroy()
            
        if score_1 >= 5 or score_2 >= 5:
            finish(win)   
            score_1 = 0
            score_2 = 0
        
        b_jogar = Button(frame_baixo, command=start, text='Jogar', width= 10, height=1,font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg= fundo, fg=co0)
        b_jogar.place(x=80, y=200)
            
        
    
    #Termina o jogo
    def finish(win):
        app_vencedor_final_1 = Label(frame_baixo, text="Fim de jogo", width=17, relief="flat", anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor_final_1.place(x=40, y=80)
        app_vencedor_final_2 = Label(frame_baixo, text="Ganhador: " + win, width=17, relief="flat", anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor_final_2.place(x=40, y=100)
        score_1 = 0
        score_2 = 0
        app_x_pontos['text']=score_1
        app_o_pontos['text']=score_2
        



    #Configuração frame_baixo

    #Linhas Verticais

    app_ = Label(frame_baixo, text='', height=23, relief="flat", pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=90, y=15)

    app_ = Label(frame_baixo, text='', height=23, relief="flat", pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=157, y=15)

    #Linhas Horizontais

    app_ = Label(frame_baixo, text=' ', width=46, relief="flat", padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=63)

    app_ = Label(frame_baixo, text=' ', width=46, relief="flat", padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=123)

    #botoes

    b_0 = Button(frame_baixo, command=lambda:control('1'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_0.place(x=30, y=15)
    b_1 = Button(frame_baixo, command=lambda:control('2'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_1.place(x=96, y=15)
    b_2 = Button(frame_baixo, command=lambda:control('3'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_2.place(x=162, y=15)
    b_3 = Button(frame_baixo, command=lambda:control('4'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_3.place(x=30, y=75)
    b_4 = Button(frame_baixo, command=lambda:control('5'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_4.place(x=96, y=75)
    b_5 = Button(frame_baixo, command=lambda:control('6'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_5.place(x=162, y=75)
    b_6 = Button(frame_baixo, command=lambda:control('7'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_6.place(x=30, y=135)
    b_7 = Button(frame_baixo, command=lambda:control('8'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_7.place(x=96, y=135)
    b_8 = Button(frame_baixo, command=lambda:control('9'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_8.place(x=162, y=135)

#Botão jogar

b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width= 10, height=1,font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg= fundo, fg=co0)
b_jogar.place(x=80, y=200)

janela.mainloop()