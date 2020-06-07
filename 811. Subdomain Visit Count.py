class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_to_visit_hash = {}
        for ele in cpdomains:
            count, domain = ele.split(' ')
            domain_list = domain.split('.')
            remain = ''
            for i in range(len(domain_list) - 1, -1, -1):
                if remain == '':
                    remain = domain_list[i] + remain
                else:
                    remain = domain_list[i] + '.' + remain

                if remain in domain_to_visit_hash:
                    domain_to_visit_hash[remain] += int(count)
                else:
                    domain_to_visit_hash[remain] = int(count)
        return [' '.join([str(ele[1]), ele[0]]) for ele in domain_to_visit_hash.items()]
