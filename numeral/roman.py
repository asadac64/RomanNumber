"""The roman numeral module"""

class NumberOutOfRange(ValueError):
    """An  extention"""
    
def to_roman(num):
    """Convert Hindo_arabic to Roman number"""
    I = ['','I','II','III','IV','V','VI','VII','VIII','IX'] #เลขหลักหน่วย 0-9
    X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'] #เลขหลักสิบ 10,20,...,90
    C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'] # เลขหลักร้อย 100,200,...,900
    M = ['','M','MM','MMM'] # เลขหลักพัน 1000-3000
    

    num_1000 = M[num // 1000]
    num_100 = C[(num % 1000) // 100]
    num_10 = X[(num % 100) // 10]
    num_1 = I[num % 10]
    
    roman = num_1000 + num_100 + num_10 + num_1
    
    return roman

   


