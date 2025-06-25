
class Solution(object):

    def rle(self,s):
          
          new_s = ""
          final_str = []
          count = 1

          for i in range(len(s)):
               print(s[i],final_str)
               if i+1<len(s):
                    if s[i]==s[i+1]:
                         count += 1
                         new_s = f"{s[i]}{count}"
                    else:
                         final_str.append(new_s if i>0 else f"{s[i]}1")
                         new_s = ""
                         count = 1
                         new_s += f"{s[i+1]}{count}"
               else:
                         final_str.append(new_s)
          print("final",final_str)
          return final_str
     
    def decode_rle(self,s):
      
          my_str = ""
          
          for i in range(len(s)):
               my_str += s[i][0]*int(s[i][1:])

          return my_str

# print(decode_rle(ss))

    def determine_chars_delete(self,ss):
          
          init_chars = self.rle(ss)
          init_len = len(ss)
          
          while init_len>20:

               step = False
               for i in range(len(init_chars)):
                    if init_len==20:break
                    freq = int(init_chars[i][1:])

                    if freq>2 and freq%3 == 0:
                         init_len -= 1
                         init_chars[i] = f"{init_chars[i][0]}{freq-1}"
               for i in range(len(init_chars)):
                    if init_len==20:break
                    freq = int(init_chars[i][1:])

                    if freq>2 and (freq-1)%3 == 0:
                         init_len -= 1
                         init_chars[i] = f"{init_chars[i][0]}{freq-1}"
                         step = True
                         break  
                    
               if step: continue
          
               for i in range(len(init_chars)):
                    if init_len==20:break
                    freq = int(init_chars[i][1:])
                    if freq > 2: 
                         init_len -= 1
                         init_chars[i] = f"{init_chars[i][0]}{freq-1}"
                         break
                    elif freq == 2:
                          continue      
                    elif freq>0:
                         init_len -= 1
                         init_chars[i] = f"{init_chars[i][0]}{freq-1}"
          return self.decode_rle(init_chars)
                  
    def check_str(self,password):
         
         check_lower = 0
         check_num = 0
         check_upper = 0

         for i in range(len(password)):
              if password[i].islower():
                   check_lower += 1
              elif password[i].isupper():
                   check_upper += 1
              elif password[i].isdigit():
                   check_num += 1
                   
         return {"check_lower":check_lower,"check_upper":check_upper,"check_nums":check_num}

    def check_length(self,password):
         if len(password) >=6 and len(password) <= 20:
              return "perfect"
         return "smaller" if len(password) < 6 else "bigger" 
    
    def assign_based_on_cond(self,test1,str_build_arr,idx,all_syms,custom=False):
                    if isinstance(str_build_arr[idx],str):
                         if not test1["check_upper"]:
                              if test1["check_lower"] > 1:
                                   str_build_arr[idx] = "A"
                                   test1["check_lower"] -= 1
                                   test1["check_upper"] += 1
                              elif test1["check_nums"] > 1:
                                   str_build_arr[idx] = "A"
                                   test1["check_lower"] -= 1
                                   test1["check_upper"] += 1
                              else:
                                   str_build_arr[idx] = "A"
                                   test1["check_upper"] += 1

                         elif not test1["check_lower"]:
                              if test1["check_upper"] > 1:
                                   str_build_arr[idx] = "a"
                                   test1["check_upper"] -= 1
                                   test1["check_lower"] += 1
                              elif test1["check_nums"] > 1:
                                   str_build_arr[idx] = "a"
                                   test1["check_lower"] -= 1
                                   test1["check_lower"] += 1
                              else:
                                    str_build_arr[idx] = "a"
                                    test1["check_lower"] += 1
                         elif not test1["check_nums"]:
                              if test1["check_upper"] > 1:
                                   str_build_arr[idx] = "1"
                                   test1["check_upper"] -= 1
                                   test1["check_nums"] +=  1
                              elif test1["check_lower"] > 1:
                                   str_build_arr[idx] = "1"
                                   test1["check_lower"] -= 1
                                   test1["check_nums"] +=  1
                              else:
                                   str_build_arr[idx] = "1"
                                   test1["check_nums"] += 1

                         elif str_build_arr[idx] not in all_syms and not custom:
                                   str_build_arr[idx] = chr(ord(str_build_arr[idx])+1) # Replace
                         elif not custom:
                                   str_build_arr[idx] = "Z"
                         else: 
                              return "somestr"
                    else:
                         return "num"
          
   
    def delete_stuff(self,my_arr,test):
          
          total_deletions = len(my_arr)-20

          new_arr = []

          for i in range(len(my_arr)):
                if test["check_lower"] > 1 and my_arr[i].islower() and total_deletions>0:
                      test["check_lower"] -= 1
                      total_deletions -= 1
                elif test["check_upper"] > 1 and my_arr[i].isupper() and total_deletions>0:
                      test["check_upper"] -= 1
                      total_deletions -= 1
                elif test["check_nums"] > 1 and my_arr[i].isdigit() and total_deletions>0:
                      test["check_nums"] -= 1
                      total_deletions -= 1
                else:
                      new_arr.append(my_arr[i])

          return  new_arr

                      
          
    def strongPasswordChecker(self, password):

          """
           :type password: str
           :rtype: int
          """
          str_build_arr = list(map(str,password))
      
          all_capitals = string.ascii_uppercase
          all_lowers = string.ascii_lowercase
          all_nums = string.digits
          all_syms = ".!"

          test1 = self.check_str(password)

          if self.check_length(password) == "smaller":
              if not test1["check_upper"] and not test1["check_lower"] and not test1["check_nums"]:
                    return 6-len(password) if len(password)<= 3 else 3
              elif (not test1["check_upper"] and not test1["check_lower"]) or (not test1["check_nums"] and not test1["check_lower"]) or not test1["check_upper"] and not test1["check_nums"]:
                    return 6-len(password) if len(password)<= 3 else 2
              else:
                    return 6-len(password) 

          count = 0

          if self.check_length(password) == "bigger":
              count = len(password)-20
              str_build_arr = list(map(str,self.determine_chars_delete(password)))

     #    if self.check_length(password) == "perfect":
               
          idx = 2
          curr_len = len(str_build_arr)
          two_passes = []

          while len(two_passes)<2:
                    if str_build_arr[idx] == str_build_arr[idx-1] and str_build_arr[idx-1] == str_build_arr[idx-2] and not len(two_passes):
                              if idx+1<len(str_build_arr) and str_build_arr[idx+1] == str_build_arr[idx]:
                                   prim = self.assign_based_on_cond(test1,str_build_arr,idx,all_syms) # Replace
                                   if not prim: count+=1
                              else:
                                   prim = self.assign_based_on_cond(test1,str_build_arr,idx,all_syms,True)
                                   if not prim: 
                                        count += 1
                                   elif prim=="somestr" and curr_len-1>6:
                                        str_build_arr[idx] = -1 # Delete
                                        curr_len -= 1
                                        count += 1
                                   else:
                                        str_build_arr[idx] = chr(ord(str_build_arr[idx-1])+1)
                                        count += 1
                              idx += 1
                    elif len(two_passes):
                                   prim = self.assign_based_on_cond(test1,str_build_arr,idx-2,all_syms,True)
                                   if not prim: 
                                             count+=1
                                   idx += 1
                    else:
                              idx += 1
                    if idx==len(str_build_arr):
                         two_passes.append(1)
                         idx = 2
          return count