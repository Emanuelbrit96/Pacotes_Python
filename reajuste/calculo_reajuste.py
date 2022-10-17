import imp


from reajuste.formatacao import formatar

def cal_reajuste(sal, percent ):
    percent = percent / 100
    reajuste = (sal * percent) + sal
    formatacao = formatar(reajuste,percent)
    return formatacao