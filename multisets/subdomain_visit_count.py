from collections import Counter


def subdomainVisits(cpdomains):
    ans = Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]


print(subdomainVisits(["9001 discuss.leetcode.com"]))
