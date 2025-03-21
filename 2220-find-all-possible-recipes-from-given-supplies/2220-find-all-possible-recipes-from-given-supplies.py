class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        check = {}
        dic_ingre = defaultdict(list)

        for i in range(len(ingredients)):
            check[recipes[i]] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                dic_ingre[ingredients[i][j]].append(recipes[i])

        cur = defaultdict(int)
        res = []

        i = 0
        while i < len(supplies):
            for rec in dic_ingre[supplies[i]]:
                cur[rec] += 1
                if cur[rec] == check[rec]:
                    res.append(rec)
                    supplies.append(rec)
            i += 1

        return res