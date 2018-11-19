# -*- coding: utf-8 -*-

#%%

products={"Guitar":"1000",
          "Pick box":"5",
          "Guitar Strings":"10",
          "Insurance":"5",
          "Priority mail":"10"}

def checkout(list):
    cost=0
    if list==[] or list==["Insurance","Priority mail"] or list==["Priority mail","Insurance"]:
        return "Please add something to your shopping cart before checkout"
    
    else:
        for product in list:
            if list.count("Insurance") > 1 or list.count("Priority mail")>1:
                return "You cant add more the one Insurance and Priority mail"
            else:   
                cost+=int(products[product])
                if cost>10000:
                    return "Please remove items from your shopping bag, you preceded the spending limit"
        return "Your cost is: " + "$" + str(cost)
    
