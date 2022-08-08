{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}


##copied this from the solution and by this command we directly come to know where will be the error.  
echo "JSON DATA" | python -m json.tool


##OUTPUT

# "payble":{ 
#             ^