# Reference - https://www.linkedin.com/pulse/justdial-phone-number-anbu-saravanan/


def get_data_bw(s, sv, ev):
    si = s.find(sv)
    if si != -1:
        ei = s.find(ev, si)
        if ei != -1:
            return s[si:ei]
    return ""


def get_sva(s):
    d = {11: "+", 12: "-", 13: ")", 14: "("}
    return d.get(s, s - 1)


def get_num(s, sd, vd, cv):
    j = s.split(sd)
    opv = ""
    for jj in j:
        k = jj.split(vd)
        if k[0] == cv:
            opv = k[1]
            break
    return opv


def return_op(st):
    ss = st.split(".")
    op = {}
    sc = 0
    for s in ss:
        if not s == "":
            sc = sc + 1
            j = s.split(":")
            cn = j[0]
            op[cn] = get_sva(sc)
    return op


def generate_number(s, m):
    stag = s.find_all("span")[1:]
    num = ""
    for sp in stag:
        icn = sp["class"][1]
        num = "{}{}".format(num, m["{}".format(icn)])
    return num
