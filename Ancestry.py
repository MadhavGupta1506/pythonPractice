def ancestry(p,present,past):
    if(present==past):
        return [present]    
    else:
        return [present]+(ancestry(P,P[present],past))
P = {

    'Jahangir': 'Akbar',

    'Akbar': 'Humayun',

    'Humayun': 'Babur'   

}

print(ancestry(P,"Jahangir","Babur"))
