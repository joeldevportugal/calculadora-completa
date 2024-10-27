import customtkinter

# Variável de controle para estado da calculadora
calculadora_ligada = True

# Funções de cálculo
def inserir_valor(valor):
    # Verifica se a calculadora está ligada antes de inserir o valor
    if calculadora_ligada:
        conteudo_atual = Ecra.get()
        Ecra.delete(0, "end")
        Ecra.insert("end", conteudo_atual + str(valor))

def limpar():
    if calculadora_ligada:
        Ecra.delete(0, "end")

def calcular():
    if calculadora_ligada:
        try:
            expressao = Ecra.get()
            resultado = eval(expressao.replace("X", "*").replace(",", "."))
            Ecra.delete(0, "end")
            Ecra.insert("end", str(resultado).replace(".", ","))
        except Exception as e:
            Ecra.delete(0, "end")
            Ecra.insert("end", "Erro")

def apagar_ultimo():
    if calculadora_ligada:
        conteudo_atual = Ecra.get()
        # Apaga o último carácter se o ecrã não estiver vazio
        if conteudo_atual:
            Ecra.delete(len(conteudo_atual) - 1, "end")



def desligar():
    global calculadora_ligada
    calculadora_ligada = False  # Atualiza estado para desligado
    Ecra.delete(0, "end")
    Ecra.insert("end", "Desligado")
    # Tornar texto dos botões invisível
    for botao in todos_botoes:
        botao.configure(text="")
      # Tornar BtnBack invisível
    BtnBack.configure(text="")


def ligar():
    global calculadora_ligada
    calculadora_ligada = True  # Atualiza estado para ligado
    limpar()
    rdDesligar.deselect()  # Desmarcar o botão "Desligar"
    
    # Restaurar o texto dos botões
    BtnSete.configure(text="7")
    Btnoito.configure(text="8")
    Btnove.configure(text="9")
    BtDiv.configure(text="/")
    Btnquatro.configure(text="4")
    Btncinco.configure(text="5")
    Btnseis.configure(text="6")
    BtnMul.configure(text="X")
    Btnum.configure(text="1")
    Btndois.configure(text="2")
    BtnTres.configure(text="3")
    Btnsub.configure(text="-")
    BtnZero.configure(text="0")
    BtnVirgula.configure(text=",")
    Btnigual.configure(text="=")
    Btnsoma.configure(text="+")
    BtnClear.configure(text="C")
    BtnCE.configure(text="CE")
    BtnBack.configure(text="⌫")
    
    

# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("220x295+100+100")
janela.resizable(0, 0)
janela.title('minha calculadora CTK © Dev Joel 2024')

# Entrada com texto alinhado à direita
Ecra = customtkinter.CTkEntry(janela, width=200, justify="right")  # Alinhado à direita
Ecra.place(x=10, y=10)

# Botões de controle
rdLigar = customtkinter.CTkRadioButton(janela, text="Ligar", command=ligar)
rdLigar.place(x=10, y=55)

rdDesligar = customtkinter.CTkRadioButton(janela, text="Desligar", command=desligar)
rdDesligar.place(x=120, y=55)

# Botões de operações e números
BtnClear = customtkinter.CTkButton(janela, text='C', width=45, command=limpar)
BtnClear.place(x=10, y=95)

BtnCE = customtkinter.CTkButton(janela, text='CE', width=45, command=limpar)
BtnCE.place(x=65, y=95)

BtnBack = customtkinter.CTkButton(janela, text='⌫', width=95, command=apagar_ultimo)
BtnBack.place(x=115, y=95)

BtnSete = customtkinter.CTkButton(janela, text="7", width=45, command=lambda: inserir_valor("7"))
BtnSete.place(x=10, y=130)

Btnoito = customtkinter.CTkButton(janela, text="8", width=45, command=lambda: inserir_valor("8"))
Btnoito.place(x=65, y=130)

Btnove = customtkinter.CTkButton(janela, text="9", width=45, command=lambda: inserir_valor("9"))
Btnove.place(x=115, y=130)

BtDiv = customtkinter.CTkButton(janela, text="/", width=45, command=lambda: inserir_valor("/"))
BtDiv.place(x=165, y=130)

Btnquatro = customtkinter.CTkButton(janela, text="4", width=45, command=lambda: inserir_valor("4"))
Btnquatro.place(x=10, y=165)

Btncinco = customtkinter.CTkButton(janela, text="5", width=45, command=lambda: inserir_valor("5"))
Btncinco.place(x=65, y=165)

Btnseis = customtkinter.CTkButton(janela, text="6", width=45, command=lambda: inserir_valor("6"))
Btnseis.place(x=115, y=165)

BtnMul = customtkinter.CTkButton(janela, text="X", width=45, command=lambda: inserir_valor("X"))
BtnMul.place(x=165, y=165)

Btnum = customtkinter.CTkButton(janela, text="1", width=45, command=lambda: inserir_valor("1"))
Btnum.place(x=10, y=200)

Btndois = customtkinter.CTkButton(janela, text="2", width=45, command=lambda: inserir_valor("2"))
Btndois.place(x=65, y=200)

BtnTres = customtkinter.CTkButton(janela, text="3", width=45, command=lambda: inserir_valor("3"))
BtnTres.place(x=115, y=200)

Btnsub = customtkinter.CTkButton(janela, text="-", width=45, command=lambda: inserir_valor("-"))
Btnsub.place(x=165, y=200)

BtnZero = customtkinter.CTkButton(janela, text="0", width=45, command=lambda: inserir_valor("0"))
BtnZero.place(x=10, y=235)

BtnVirgula = customtkinter.CTkButton(janela, text=",", width=45, command=lambda: inserir_valor(","))
BtnVirgula.place(x=65, y=235)

Btnigual = customtkinter.CTkButton(janela, text="=", width=45, command=calcular)
Btnigual.place(x=115, y=235)

Btnsoma = customtkinter.CTkButton(janela, text="+", width=45, command=lambda: inserir_valor("+"))
Btnsoma.place(x=165, y=235)

# Lista para todos os botões
todos_botoes = [
    BtnSete, Btnoito, Btnove, BtDiv, Btnquatro, Btncinco, Btnseis, BtnMul,
    Btnum, Btndois, BtnTres, Btnsub, BtnZero, BtnVirgula, Btnigual, Btnsoma, BtnClear, BtnCE
]

Autor = customtkinter.CTkLabel(janela, text='Autor : DevJoel 2024 © Portugal', font=("Arial", 14))  
Autor.place(x=10, y=265)

# Executa a janela principal
janela.mainloop()