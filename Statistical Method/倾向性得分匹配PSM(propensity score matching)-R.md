# 一、倾向性得分匹配(PSM)



```R
library(haven)
library(pastecs)
da <- read.csv("I:/MIMIC/PneumoniaData/30/dat_A.csv")
cols <- c('WBCs', 'NEUT', 'LYMPH', 'MONO', 'PLT', 'HGB', 'PT', 'FIB', 'ALB', 'ALT', 'AST', 'TB', 
          'DBIL', 'BUN', 'Cre', 'CK', 'LDH', 'Tn', 'GLU', 'UA', 'BNP', 'T(C)', 'TP', 'CRP', 'DDI', 
          'Smoking', 'Cough', 'ShortnessOfBreath', 'Headache', 'Diarrhea', 'ChestPain', 
          'Fever', 'HeartDisease', 'Diabetes', 
          'Oseltamivir', 'Ribavirin', 'Ganciclovir', 'Methylprednisolone', 'Prednisone', 
          'Moxifloxacin', 'Ceftazidime', 'Fluconazole', 'Levofloxacin', 'Azithromycin', 
          'Ceftriaxone', 'Amoxicillin', 'Age', 'M')
by(da[cols],da$label,function(x)stat.desc(x,norm=TRUE))
by(da[cols],da$label,summary)

library(pastecs)
by(da[cols],da$label,stat.desc)

# wilcox.test(gre~admit,data=da)
Chi<-table(da$gre,da$admit)
Chi
chisq.test(Chi)




library(MatchIt)
psm.out<-matchit(label~WBCs+NEUT+LYMPH+MONO+PLT+HGB+PT+FIB+ALB+ALT+AST+TB+DBIL+BUN+Cre+CK+LDH+Tn+GLU+UA+BNP+T+TP+CRP
             +DDI+Smoking+Cough+ShortnessOfBreath+Headache+Diarrhea+ChestPain+Fever+HeartDisease+Diabetes+
               Oseltamivir+Ribavirin+Ganciclovir+Methylprednisolone+Prednisone+Moxifloxacin+Ceftazidime+
               Fluconazole+Levofloxacin+Azithromycin+Ceftriaxone+Amoxicillin+Age+M, 
             data=da, method="nearest",caliper=0.2)
psm.out
summary(psm.out)
library(ggplot2)
plot(psm.out, type = "jitter")
plot(psm.out, type = "hist")
m.data1 <- match.data (psm.out)
write.csv (m.data1, file = "I:/MIMIC/PneumoniaData/30/match_nearest.csv)

```

