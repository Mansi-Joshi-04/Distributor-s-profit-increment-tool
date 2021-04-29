from itertools import combinations,chain
from Hashing import Hash_Map
class Apriori:
    def __init__(self,minsuppt,minconf,filename):
        self.minsuppt=minsuppt
        self.minconf=minconf
        self.Filename=filename
    def load_file(self):
        transactions=[]
        f = open(self.Filename, "r")
        for i in f:
            stripped_line=i.strip()
            line_list=stripped_line.split(",")
            transactions.append(line_list)
        f.close()
        return transactions
    def order_unique(self):
        r=self.load_file()
        order=[]
        for i in r:
            for item in i:
                if item not in order:
                    order.append(item)
        return order
    def count_occurences(self,itemset):
        count=0
        transactionv=self.load_file()
        for i in range(len(self.load_file())):
            if set(itemset).issubset(set(transactionv[i])):
                count+=1
        return count
    def get_frequent(self,itemsets,prev_discarded):
        transac =self.load_file()
        num_trans=len(transac)
        L=[]
        suppt_count=[]
        new_discarded=[]
        k=len(prev_discarded.keys())
        for i in range(len(itemsets)):
            discarded_before=False
            if k>0:
                for it in prev_discarded[k]:
                    if set(it).issubset(set(itemsets[i])):
                        discarded_before=True
                        break
            if not discarded_before:
               count=self.count_occurences(itemsets[i])
               if count/num_trans>=self.minsuppt:
                  L.append(itemsets[i])
                  suppt_count.append(count)
               else:
                  new_discarded.append(itemsets[i])
        return L,suppt_count,new_discarded
        
    def print_table(self,T,supp_count):
            print("Itemset|Frequency")
            for k in range(len(T)):
                print("{}:{}".format(T[k],supp_count[k]))
            print("\n\n")
    def L1(self):
        C={}
        L={}
        itemset_size=1
        C.update({itemset_size:[[i] for i in self.order_unique()]})
        Discarded={itemset_size:[]}
        supp_count_L={}
        f,sup,new_discarded=self.get_frequent(C[itemset_size],Discarded)
        Discarded.update({itemset_size:new_discarded})
        L.update({itemset_size:f})
        supp_count_L.update({itemset_size:sup})
        print("L1:")
        self.print_table(L[1],supp_count_L[1])
        return L[1]
    def join_two_itemsets(self,it1,it2,order):
       d=self.order_unique()
       it1.sort(key=lambda x:d.index(x))
       it2.sort(key=lambda x:d.index(x))
       for i in range(len(it1)-1):
           if it1[i]!=it2[i]:
               return []
       if d.index(it1[-1])<d.index(it2[-1]):
          return it1+[it2[-1]]
       return []
    def join_set_itemsets(self,set_of_its,order):
        C=[]
        for i in range(len(set_of_its)):
            for j in range(i+1,len(set_of_its)):
                it_out=self.join_two_itemsets(set_of_its[i],set_of_its[j],self.order_unique())
                if len(it_out)>0:
                    C.append(it_out)
        return C
    def powerset(self,s):
         return list(chain.from_iterable(combinations(s,r)for r in range(1,len(s)+1)))
                     
    def write_rules(self,X,X_S,S,conf,supp,lift,num_transactions):
         transac =self.load_file()
         num_trans=len(transac)
         out_rules=""
         out_rules+="Freq.Itemset:{}\n".format(X)
         out_rules+="  Rule:{} ->{} \n".format(list(S),list(X_S))
         out_rules+="  Conf:{0:2.3f} ".format(conf)
         out_rules+="  supp:{0:2.3f} ".format(supp/num_trans)
         out_rules+="  Lift:{0:2.3f} \n".format(lift)
         return out_rules
       
    def CkLkAr(self):
        itemset_size=1
        C={}
        CI={}
        L={}
        new_discarded=[]
        supp_count_L={}
        k=itemset_size+1
        temp=self.L1()
        transac =self.load_file()
        num_trans=len(transac)
        L.update({itemset_size:temp})
        CI.update({itemset_size:[[i] for i in self.order_unique()]})
        Discarded={itemset_size:[]}
        convergence=False
        while not convergence:
            joins=self.join_set_itemsets(L[k-1],self.order_unique())
            C.update({k:joins})
            print("table C{}:\n".format(k))
            self.print_table(C[k],[self.count_occurences(it)for it in C[k]])
            t=Hash_Map()
            t.hash_key(C[k],[self.count_occurences(it)for it in C[k]])
            Ck=t.print()
            CI.update({k:Ck})
            f,sup,new_Discarded=self.get_frequent(CI[k],Discarded)
            Discarded.update({k:new_discarded})
            L.update({k:f})
            supp_count_L.update({k:sup})
            if len(L[k])==0:
               convergence=True
            else:
                print("table L{}:\n".format(k))
                self.print_table(L[k],supp_count_L[k])
            k+=1
            assoc_rules_str=""
        for i in range(1,len(L)):
            for j in range(len(L[i])):
                Y=set(L[i][j])
                s=list(self.powerset(Y))
                s.pop()
                for z in s:
                    S=set(z)
                    X=set(L[i][j])
                    X_S=set(X-S)
                    sup_x=self.count_occurences(X)
                    sup_x_s=self.count_occurences(X_S)
                    conf=sup_x/self.count_occurences(S)
                    lift=conf/(sup_x_s/num_trans)
                    if conf>=self.minconf and sup_x>=self.minsuppt:
                         assoc_rules_str+=self.write_rules(X,X-S,S,conf,sup_x,lift,num_trans)
            print(assoc_rules_str)