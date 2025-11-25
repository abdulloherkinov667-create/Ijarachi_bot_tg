from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class KvartiraBosh(StatesGroup):
    kvartira_tan = State()
    muddat_ijara = State()
    manzil = State()
    kimlarga_k= State()
    xona_soni= State()    
    maydoni = State()    
    tamir = State()    
    jihoz_uyda= State()    
    kvar_narx= State()   
    kvar_vosita= State()    
    user_tel = State() 
    izoh_user = State()         
    user_tel = State()         
            
    