
def parseInformation():
    numbers = str(input())
    information = numbers.split()
    return information
    

def calculateTax(wages, interest, unemployment, status, taxwithheld, taxableincome):
    #single filers
    if status == 1:
        if 0 < taxableincome < 10000:
            return round(taxableincome / 100 * 10)
        if 10001 < taxableincome <  40000:
            return round(1000 + ((taxableincome - 10000) / 100 * 12))
        if 40001 < taxableincome < 85000:
            return round(4600 + ((taxableincome - 40000) / 100 * 22))
        if taxableincome > 80000:
           return round(14500 + ((taxableincome - 85000) / 100 * 24)) 
    
    
    #married filers
    if status == 2:
        if 0 < taxableincome < 20000:
            return round(taxableincome / 100 * 10)
        if 20001 < taxableincome < 80000:
            return round(2000 + ((taxableincome - 20000) / 100 * 12))
        if taxableincome > 80000:
            return round(9200 + ((taxableincome - 80000) / 100 * 22))
    return 0        
            
            
def main():
    information = parseInformation()
    wages = int(information[0])
    taxInterest = int(information[1])
    unemployment = int(information[2])
    status = int(information[3])
    taxWithheld = int(information[4])    
  
 
    agi = wages + taxInterest + unemployment
    print(f"AGI: ${agi:,}")
    if agi > 120000:
        print("Error: Income too high to use this form")
    else:
        deduction = 0
        if status == 1:
            deduction = 12000
        else:
            deduction = 24000
        print(f"Deduction: ${deduction:,}")
        taxableincome = agi - deduction
        if taxableincome < 0:
            taxableincome = 0
        print(f"Taxable income: ${taxableincome:,}")
        if taxableincome == 0:
            quit()
        tax = calculateTax(wages, taxInterest, unemployment, status, taxWithheld, taxableincome)
        print(f"Federal tax: ${tax:,}")
        taxDue = tax - taxWithheld
        if taxDue < 0:
            print(f"Tax refund: ${abs(taxDue):,}")
            
            
main()
    
