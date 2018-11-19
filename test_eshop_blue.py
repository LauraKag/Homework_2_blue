# -*- coding: utf-8 -*-

#%%

from eshop_blue import checkout

def test_eshop_blue_normalorder():
    normalorder1=["Pick box","Guitar","Guitar Strings"]
    normalorder2=["Pick box","Guitar","Guitar Strings","Insurance","Priority mail"]
    
    assert checkout(normalorder1)=="Your cost is: $1015"
    assert checkout(normalorder2)=="Your cost is: $1030"
    
def test_eshop_blue_emptycart():
    emptycart=[]
    
    assert checkout(emptycart)=="Please add something to your shopping cart before checkout"

def test_eshop_blue_only_Insurance_or_Prioritymail():
    order1=["Insurance","Priority mail"]
    order2=["Priority mail","Insurance"]
    
    assert checkout(order1)=="Please add something to your shopping cart before checkout"
    assert checkout(order2)=="Please add something to your shopping cart before checkout"

def test_eshop_blue_morethanonce_Insurance_or_Prioritymail():
    order1=["Pick box","Guitar","Guitar Strings","Insurance","Priority mail","Priority mail"]
    order2=["Pick box","Guitar","Guitar Strings","Insurance","Insurance","Priority mail","Priority mail"]
    
    assert checkout(order1)=="You cant add more the one Insurance and Priority mail"
    assert checkout(order2)=="You cant add more the one Insurance and Priority mail"
    
def test_eshop_blue_preceding_spending_limit():
    tooexpensivecart=["Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Pick box"]
    
    assert checkout(tooexpensivecart)=="Please remove items from your shopping bag, you preceded the spending limit"