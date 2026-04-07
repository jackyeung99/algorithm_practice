class Solution:
    def countSeniors(self, details: List[str]) -> int:
        

        count = 0
        for pas in details:


            phone = pas[:10]
            gender = pas[10]
            age = pas[11:13]

            print(phone, gender, age)
            if int(age) > 60: 

                count += 1


        return count