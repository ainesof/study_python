def returnSQL(para):
    # --------------------------------------------------- common
    if para == 'tableParityCheck':
        sql = tableParityCheck()
    elif para == 'findGroup':
        sql = findGroup()
    elif para == 'tab5_recentlyDateSearchQuery':
        sql = tab5_recentlyDateSearchQuery()
    elif para == 'find_SuikjaSearchQuery':
        sql = find_SuikjaSearchQuery()
    elif para == 'tab5_headerDateSearchQuery':
        sql = tab5_headerDateSearchQuery()

    # --------------------------------------------------- tab5_view
    elif para == 'tab5_viewCommonSearchQuery':
        sql = tab5_viewCommonSearchQuery()
    elif para == 'tab5_view1Table1':
        sql = tab5_view1Table1()
    elif para == 'tab5_view1Table2':
        sql = tab5_view1Table2()
    elif para == 'tab5_view2Table':
        sql = tab5_view2Table()
    # ---------------------------------------------------- tab5_group
    elif para == 'tab5_groupCommonSearchQuery':
        sql = tab5_groupCommonSearchQuery()
    # ---------------------------------------------------- tab5_item
    elif para == 'tab5_itemCommonSearchQuery':
        sql = tab5_itemCommonSearchQuery()
    # ---------------------------------------------------- tab5_suikja
    elif para == 'tab5_suikjaSearchQuery1':
        sql = tab5_suikjaSearchQuery1()
    # ---------------------------------------------------- 미사용
    elif para == 'tab5_viewSearchQuery_old':
        sql = tab5_viewSearchQuery_old()
    elif para == 'tab5_view1SearchQuery1':
        sql = tab5_view1SearchQuery1()
    elif para == 'tab5_view2SearchQuery1':
        sql = tab5_view2SearchQuery1()
    elif para == 'tab5_win1SearchQuery_old':
        sql = tab5_win1SearchQuery_old()
    elif para == 'tab5_group1SearchQuery1':
        sql = tab5_group1SearchQuery1()
    elif para == 'tab5_group2SearchQuery1':
        sql = tab5_group2SearchQuery1()
    elif para == 'tab5_items1SearchQuery1_old':
        sql = tab5_items1SearchQuery1_old()
    return sql



def tableParityCheck():
    """조회값 하나펀드 자료테이블과 비교"""
    str = \
"""
/* tableParityCheck */

select rownum,a.FUND_CD,a.suik_set_money,decode(a.suik_set_money-b.suik_set_money,0,'True',b.suik_set_money) as parity 
from (
    select rownum as idx, 
    decode(rownum,1,'1236',2,'1280',3,'1281',4,'1282',5,'1283',6,'1556',7,'1944',
    8,'1959',9,'1961',10,'1980',11,'4001',12,'4003',13,'5555',14,'5832',15,'DD43',16,'DD45',17,'DD47',
    18,'DD49',19,'DD97',20,'ER11',21,'ER22',22,'ER23',23,'GE01',25,'HS01',26,'KL21',27,'NPS4',
    28,'PM01',29,'RW01',30,'SC01',31,'SC02',32,'SC07',33,'SS07',34,'TP01',35,'TY01',36,'TY03',37,'TY04',38,'TY21'
    ) as FUND_CD
    from dual
    connect by level<=40
) x,
(
    select a.FUND_CD,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as suik_set_money
    from SUIKJA_INFO a,FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd='{date}' and a.fund_cd<>'1522'
    group by a.FUND_CD
) a,(
    select 펀드코드,sum(설정금액) as suik_set_money
    from 펀드_기준가격
    where 기준일자='{date}'
    group by 펀드코드
)b
where x.FUND_CD=a.FUND_CD and x.FUND_CD=b.펀드코드
"""
    return str

def findGroup():
    """ 수익자로 고객그룹을 찾음"""
    str = \
"""
/* findGroup */

select max(suik_group)
from SUIKJA_INFO
where suik_name='{suikja}'
group by suik_group
"""
    return str


def tab5_recentlyDateSearchQuery():
    """최근 DB자료 날짜"""
    str = \
"""
/* tab5_recentlyDateSearchQuery */

select to_char(max(a.tr_ymd),'yyyy-mm-dd')
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
"""
    return str

def find_SuikjaSearchQuery():
    """고객명 찾기"""
    str = \
"""
/* find_SuikjaSearchQuery */

select suik_group,suik_name
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 
and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and suik_name like'%{suikja}%'
group by suik_group,suik_name
"""
    return str


def tab5_headerDateSearchQuery():
    """날짜 조회"""
    str = \
"""
/* tab5_headerDateSearchQuery */

select ' ','기준일자',
        substr('{date}',3,10) as today,
        substr(to_char(last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)),'yyyy-mm-dd'),3,10) as lastmonth,
        substr(to_char(last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01','04','04',
        '05','04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1),'yyyy-mm-dd'),3,10) as lastquater,
        substr(to_char(to_date(substr('{date}',0,4)-1||'/12/31'),'yyyy-mm-dd'),3,10) as lastyear,
        substr(to_char(to_date(substr('{date}',0,4)-2||'/12/31'),'yyyy-mm-dd'),3,10) as last2year
from dual
"""
    return str


#   ----------------------------------------------

def tab5_view1Table1():
    """1테이블"""
    str = \
"""
select rownum as idx, decode(rownum,1,'NPS',2,'공제회',3,'금융일반',4,'생보사',5,'손보사',6,'연기금',7,'은행',8,'일반법인',9,'자산운용',10,'저축은행',11,'중앙회',12,'증권') suik_group
from dual connect by level<=12
"""
    return str

def tab5_view1Table2():
    """1테이블"""
    str = \
"""
select rownum as idx, decode(rownum,1,'공제회',2,'금융일반',3,'생보사',4,'손보사',5,'연기금',6,'은행',7,'일반법인',8,'자산운용',9,'저축은행',10,'중앙회',11,'증권',12,'') suik_group
from dual connect by level<=12
"""
    return str

def tab5_view2Table():
    """2테이블"""
    str = \
"""
select rownum as idx, decode(rownum,1,'채권형',2,'주식형',3,'글로벌') SUIK_FUND_TYPE
from dual connect by level<=3
"""
    return str

def tab5_viewCommonSearchQuery():
    """테이블 자료수 조회"""
    str = \
"""

/* tab5_viewCommonSearchQuery */

select decode({val},'','합계',{val}), sum(bu_sum),
sum(TODAY), sum(LASTMONTH), sum(LASTQUATER), sum(LASTYEAR),
sum(TODAY2), sum(LASTMONTH2), sum(LASTQUATER2), sum(LASTYEAR2)
from(
    select idx,{val},today+today2 as bu_sum,today,today-lastmonth as lastmonth,today-lastquater as lastquater,today-lastyear as lastyear,
    today2,today2-lastmonth2 as lastmonth2,today2-lastquater2 as lastquater2,today2-lastyear2 as lastyear2
    from(
        select idx,A.{val}, A.today, A.lastmonth, A.lastquater, A.lastyear,B.today2, B.lastmonth2, B.lastquater2, B.lastyear2
        from(
            select idx, x.{val}, nvl(a.today,0) today, nvl(b.lastmonth,0) lastmonth,
            nvl(c.lastquater,0) lastquater, nvl(d.lastyear,0) lastyear
            from( {table1} ) x,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as today
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.{val}
                ) a,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.{val}
                ) b,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05',
                '04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.{val}
                ) c,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.{val}
                ) d
            where x.{val}=a.{val}(+) and x.{val}=b.{val}(+) and x.{val}=c.{val}(+) and x.{val}=d.{val}(+)
            ) A,
            (
            select decode(x.{val},'연기금','NPS','','연기금',x.{val}) as {val}, nvl(a.today2,0) today2, nvl(b.lastmonth2,0) lastmonth2,
            nvl(c.lastquater2,0) lastquater2, nvl(d.lastyear2,0) lastyear2
            from( {table2} ) x,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) today2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.{val}
                ) a,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.{val}
                ) b,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01','04','04',
                '05','04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.{val}
                ) c,(
                select a.{val},decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.{val}
                ) d
            where x.{val}=b.{val}(+) and x.{val}=a.{val}(+) and x.{val}=c.{val}(+) and x.{val}=d.{val}(+)
            ) B
        where a.{val}=b.{val}(+)
        order by idx
        )
    )
group by rollup({val})

"""
    return str

def tab5_groupCommonSearchQuery():
    """테이블 자료수 조회"""
    str = \
"""
/* tab5_groupCommonSearchQuery */

select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
decode(a.{val},'',decode(b.{val},'',decode(c.{val},'',decode(d.{val},'',e.{val},d.{val}),c.{val}),b.{val}),a.{val}) {val},
nvl(a.suik_set_money,0) as suik_set_money,
nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY,
nvl(a.SUIK_NET_MONEY-b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,
nvl(a.SUIK_NET_MONEY-c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
nvl(a.SUIK_NET_MONEY-d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3,
nvl(a.SUIK_NET_MONEY-e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
from(
    select a.tr_ymd,a.suik_name,a.{val},a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd like'%{nps}%' and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd='{date}'and a.{val2}='{select}' and a.suik_mg_bu='{mg_bu}'
) a full outer join (
    select a.tr_ymd,a.suik_name,a.{val},a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd like'%{nps}%' and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.{val2}='{select}' and a.suik_mg_bu='{mg_bu}'
) b
on  a.SUIK_NAME=b.SUIK_NAME and a.{val}=b.{val} and a.FUND_CD=b.FUND_CD and a.SUIK_SEQ=b.SUIK_SEQ
full outer join (
    select a.tr_ymd,a.suik_name,a.{val},a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd like'%{nps}%' and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
    '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
    and a.{val2}='{select}' and a.suik_mg_bu='{mg_bu}'
 ) c
on a.SUIK_NAME=c.SUIK_NAME and a.{val}=c.{val} and a.FUND_CD=c.FUND_CD and a.SUIK_SEQ=c.SUIK_SEQ
full outer join (
    select a.tr_ymd,a.suik_name,a.{val},a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd like'%{nps}%' and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')and a.{val2}='{select}' and a.suik_mg_bu='{mg_bu}'
) d
on a.SUIK_NAME=d.SUIK_NAME and a.{val}=d.{val} and a.FUND_CD=d.FUND_CD and a.SUIK_SEQ=d.SUIK_SEQ
full outer join (
    select a.tr_ymd,a.suik_name,a.{val},a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd like'%{nps}%' and a.SUIK_FUND_TYPE is not null
    and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')and a.{val2}='{select}' and a.suik_mg_bu='{mg_bu}'
) e
on a.SUIK_NAME=e.SUIK_NAME and a.{val}=e.{val} and a.FUND_CD=e.FUND_CD and a.SUIK_SEQ=e.SUIK_SEQ
order by SUIK_NAME, {val}
"""
    return str


def tab5_itemCommonSearchQuery():
    """펀드정보까지 보여주는 조회"""
    str = \
"""
/* tab5_itemCommonSearchQuery */

select a.SUIK_NAME,a.suik_group,a.SUIK_FUND_TYPE,a.fund_cd,fund_nm,suik_set_money,
SUIK_SET_MONEYSUM1,SUIK_SET_MONEYSUM2,SUIK_SET_MONEYSUM3,SUIK_SET_MONEYSUM4,
suik_set_money1,suik_set_money2,suik_set_money3,suik_set_money4
from(
    select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
    decode(a.suik_group,'',decode(b.suik_group,'',decode(c.suik_group,'',decode(d.suik_group,'',e.suik_group,d.suik_group),c.suik_group),b.suik_group),a.suik_group) suik_group,
    decode(a.SUIK_FUND_TYPE,'',decode(b.SUIK_FUND_TYPE,'',decode(c.SUIK_FUND_TYPE,'',decode(d.SUIK_FUND_TYPE,'',e.SUIK_FUND_TYPE,d.SUIK_FUND_TYPE),c.SUIK_FUND_TYPE),b.SUIK_FUND_TYPE),a.SUIK_FUND_TYPE) SUIK_FUND_TYPE,
    decode(a.fund_cd,'',decode(b.fund_cd,'',decode(c.fund_cd,'',decode(d.fund_cd,'',e.fund_cd,d.fund_cd),c.fund_cd),b.fund_cd),a.fund_cd) fund_cd,
    nvl(a.suik_set_money,0) as suik_set_money,
    nvl(a.suik_set_money-b.suik_set_money,0) as SUIK_SET_MONEYSUM1,
    nvl(a.suik_set_money-c.suik_set_money,0) as SUIK_SET_MONEYSUM2,
    nvl(a.suik_set_money-d.suik_set_money,0) as SUIK_SET_MONEYSUM3,
    nvl(a.suik_set_money-e.suik_set_money,0) as SUIK_SET_MONEYSUM4,
    nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
    nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
    from(
        select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd='{date}'
        group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
        ) a full outer join (
        select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month))
        group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
        ) b
        on  a.SUIK_NAME=b.SUIK_NAME and a.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE and a.FUND_CD=b.FUND_CD
        full outer join (
        select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
        '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
        group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
         ) c
        on a.SUIK_NAME=c.SUIK_NAME and a.SUIK_FUND_TYPE=c.SUIK_FUND_TYPE and a.FUND_CD=c.FUND_CD
        full outer join (
        select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')
        group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
        ) d
        on a.SUIK_NAME=d.SUIK_NAME and a.SUIK_FUND_TYPE=d.SUIK_FUND_TYPE and a.FUND_CD=d.FUND_CD
        full outer join (
        select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')
        group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
    ) e
    on a.SUIK_NAME=e.SUIK_NAME and a.SUIK_FUND_TYPE=e.SUIK_FUND_TYPE and a.FUND_CD=e.FUND_CD
    ) A, (
    select FUND_CD,fund_nm,tr_ymd
    from  FUND_BASIC a
    where tr_ymd=(select max(tr_ymd)
                    from FUND_BASIC
                    where a.FUND_CD=FUND_CD)
    ) B
where A.fund_cd=B.fund_cd
order by a.FUND_CD, fund_nm


   
"""
    return str

def tab5_suikjaSearchQuery1():
    """다이렉트로 수익자정보 검색"""
    str= \
"""
/* tab5_group2SearchQuery1 */

select a.fund_cd,b.fund_nm,SUIK_FUND_TYPE, suik_set_money, SUIK_NET_MONEY, 
SUIK_NET_MONEY1, SUIK_NET_MONEY2, SUIK_NET_MONEY3, SUIK_NET_MONEY4,
suik_set_money1, suik_set_money2, suik_set_money3, suik_set_money4
from(
    select a.tr_ymd, decode(a.fund_cd,'',decode(b.fund_cd,'',decode(c.fund_cd,'',decode(d.fund_cd,'',e.fund_cd,d.fund_cd),c.fund_cd),b.fund_cd),a.fund_cd) fund_cd,
    decode(a.SUIK_FUND_TYPE,'',decode(b.SUIK_FUND_TYPE,'',decode(c.SUIK_FUND_TYPE,'',decode(d.SUIK_FUND_TYPE,'',e.SUIK_FUND_TYPE,d.SUIK_FUND_TYPE),
    c.SUIK_FUND_TYPE),b.SUIK_FUND_TYPE),a.SUIK_FUND_TYPE) SUIK_FUND_TYPE,
    nvl(a.suik_set_money,0) as suik_set_money,nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY,
    nvl(a.SUIK_NET_MONEY-b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,
    nvl(a.SUIK_NET_MONEY-c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
    nvl(a.SUIK_NET_MONEY-d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3,
    nvl(a.SUIK_NET_MONEY-e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
    nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
    nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
    from(
        select a.tr_ymd,a.fund_cd,a.SUIK_FUND_TYPE,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
        sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null 
        and a.suik_name like '%{suikja}%'
        and a.tr_ymd='{date}'
        group by a.tr_ymd,a.FUND_CD,a.SUIK_FUND_TYPE
    ) a full outer join(
        select a.tr_ymd,a.fund_cd,a.SUIK_FUND_TYPE,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
        sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null 
        and a.suik_name like '%{suikja}%'
        and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month))
        group by a.tr_ymd,a.FUND_CD,a.SUIK_FUND_TYPE
        ) b
    on  a.FUND_CD=b.FUND_CD
    full outer join(
        select a.tr_ymd,a.fund_cd,a.SUIK_FUND_TYPE,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
        sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null 
        and a.suik_name like '%{suikja}%'
        and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
        '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
        group by a.tr_ymd,a.FUND_CD,a.SUIK_FUND_TYPE
        ) c
    on a.FUND_CD=c.FUND_CD
    full outer join(
        select a.tr_ymd,a.fund_cd,a.SUIK_FUND_TYPE,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
        sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null 
        and a.suik_name like '%{suikja}%'
        and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')
        group by a.tr_ymd,a.FUND_CD,a.SUIK_FUND_TYPE
        ) d
    on a.FUND_CD=d.FUND_CD
    full outer join(
        select a.tr_ymd,a.fund_cd,a.SUIK_FUND_TYPE,
        sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
        sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null 
        and a.suik_name like '%{suikja}%'
        and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')
        group by a.tr_ymd,a.FUND_CD,a.SUIK_FUND_TYPE
    ) e
    on a.FUND_CD=e.FUND_CD
    order by a.FUND_CD
) A, (
    select FUND_CD,fund_nm,tr_ymd
    from  FUND_BASIC a
    where tr_ymd=(select max(tr_ymd)
                    from FUND_BASIC
                    where a.FUND_CD=FUND_CD)
    order by tr_ymd desc         
    ) B
where A.fund_cd=B.fund_cd
order by FUND_CD, fund_nm
"""
    return str


# --------------------------------------- 미사용

def tab5_viewSearchQuery_old():
    """탭5"""
    str = \
"""  
/* tab5_viewSearchQuery_old */

select decode(SUIK_GROUP,'','합계',SUIK_GROUP), sum(bu_sum),
sum(TODAY), sum(LASTMONTH), sum(LASTQUATER), sum(LASTYEAR), 
sum(TODAY2), sum(LASTMONTH2), sum(LASTQUATER2), sum(LASTYEAR2)
from(
select idx,suik_group,today+today2 as bu_sum,today,today-lastmonth as lastmonth,today-lastquater as lastquater,today-lastyear as lastyear,
today2,today2-lastmonth2 as lastmonth2,today2-lastquater2 as lastquater2,today2-lastyear2 as lastyear2
from(
select idx,A.suik_group, A.today, A.lastmonth, A.lastquater, A.lastyear,B.today2, B.lastmonth2, B.lastquater2, B.lastyear2
from(
select idx, x.suik_group, nvl(a.today,0) today, nvl(b.lastmonth,0) lastmonth,
nvl(c.lastquater,0) lastquater, nvl(d.lastyear,0) lastyear
from(
select rownum as idx, decode(rownum,1,'NPS',2,'공제회',3,'금융일반',4,'생보사',5,'손보사',6,'연기금',7,'은행',8,'일반법인',9,'자산운용',10,'저축은행',11,'중앙회',12,'증권') suik_group
from dual connect by level<=12
) x,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as today
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='1본부'
group by a.suik_group
) a,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth 
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='1본부'
group by a.suik_group 
) b,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater 
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05',
'04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='1본부'
group by a.suik_group
) c,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='1본부'
group by a.suik_group
) d
where x.suik_group=a.suik_group(+) and x.suik_group=b.suik_group(+) and x.suik_group=c.suik_group(+) and x.suik_group=d.suik_group(+)
) A,
(
select decode(x.suik_group,'연기금','NPS','','연기금',x.suik_group) as suik_group, nvl(a.today2,0) today2, nvl(b.lastmonth2,0) lastmonth2,
nvl(c.lastquater2,0) lastquater2, nvl(d.lastyear2,0) lastyear2
from(
select rownum as idx, decode(rownum,1,'공제회',2,'금융일반',3,'생보사',4,'손보사',5,'연기금',6,'은행',7,'일반법인',8,'자산운용',9,'저축은행',10,'중앙회',11,'증권',12,'') suik_group
from dual connect by level<=12
) x,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) today2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='2본부'
group by a.suik_group
) a,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_group<>'MMF' 
and a.suik_mg_bu='2본부'
group by a.suik_group
) b,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01','04','04',
'05','04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='2본부'
group by a.suik_group
) c,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and b.inte_fund_type is not null
and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_group<>'MMF' and a.suik_mg_bu='2본부'
group by a.suik_group
) d
where x.suik_group=b.suik_group(+) and x.suik_group=a.suik_group(+) and x.suik_group=c.suik_group(+) and x.suik_group=d.suik_group(+)
) B
where a.suik_group=b.suik_group(+)
order by idx
))
group by rollup(SUIK_GROUP)
"""
    return str


def tab5_view1SearchQuery1():
    """inte_fund_type를 SUIK_FUND_TYPE로 기준 고침"""
    str = \
"""  
/* tab5_view1SearchQuery1 */

select decode(SUIK_GROUP,'','합계',SUIK_GROUP), sum(bu_sum),
sum(TODAY), sum(LASTMONTH), sum(LASTQUATER), sum(LASTYEAR), 
sum(TODAY2), sum(LASTMONTH2), sum(LASTQUATER2), sum(LASTYEAR2)
from(
select idx,suik_group,today+today2 as bu_sum,today,today-lastmonth as lastmonth,today-lastquater as lastquater,today-lastyear as lastyear,
today2,today2-lastmonth2 as lastmonth2,today2-lastquater2 as lastquater2,today2-lastyear2 as lastyear2
from(
select idx,A.suik_group, A.today, A.lastmonth, A.lastquater, A.lastyear,B.today2, B.lastmonth2, B.lastquater2, B.lastyear2
from(
select idx, x.suik_group, nvl(a.today,0) today, nvl(b.lastmonth,0) lastmonth,
nvl(c.lastquater,0) lastquater, nvl(d.lastyear,0) lastyear
from(
select rownum as idx, decode(rownum,1,'NPS',2,'공제회',3,'금융일반',4,'생보사',5,'손보사',6,'연기금',7,'은행',8,'일반법인',9,'자산운용',10,'저축은행',11,'중앙회',12,'증권') suik_group
from dual connect by level<=12
) x,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as today
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
group by a.suik_group
) a,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth 
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
group by a.suik_group 
) b,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater 
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05',
'04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
group by a.suik_group
) c,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
group by a.suik_group
) d
where x.suik_group=a.suik_group(+) and x.suik_group=b.suik_group(+) and x.suik_group=c.suik_group(+) and x.suik_group=d.suik_group(+)
) A,
(
select decode(x.suik_group,'연기금','NPS','','연기금',x.suik_group) as suik_group, nvl(a.today2,0) today2, nvl(b.lastmonth2,0) lastmonth2,
nvl(c.lastquater2,0) lastquater2, nvl(d.lastyear2,0) lastyear2
from(
select rownum as idx, decode(rownum,1,'공제회',2,'금융일반',3,'생보사',4,'손보사',5,'연기금',6,'은행',7,'일반법인',8,'자산운용',9,'저축은행',10,'중앙회',11,'증권',12,'') suik_group
from dual connect by level<=12
) x,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) today2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
group by a.suik_group
) a,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
group by a.suik_group
) b,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01','04','04',
'05','04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
group by a.suik_group
) c,(
select a.suik_group,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear2
from SUIKJA_INFO a,FUND_INTEGRATE b
where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
group by a.suik_group
) d
where x.suik_group=b.suik_group(+) and x.suik_group=a.suik_group(+) and x.suik_group=c.suik_group(+) and x.suik_group=d.suik_group(+)
) B
where a.suik_group=b.suik_group(+)
order by idx
))
group by rollup(SUIK_GROUP)
"""
    return str

def tab5_view2SearchQuery1():
    """유형별 현황"""
    str=\
"""
/* tab5_view2SearchQuery1 */

select decode(SUIK_FUND_TYPE,'','합계',SUIK_FUND_TYPE), sum(bu_sum),
sum(TODAY), sum(LASTMONTH), sum(LASTQUATER), sum(LASTYEAR),
sum(TODAY2), sum(LASTMONTH2), sum(LASTQUATER2), sum(LASTYEAR2)
from(
    select idx,SUIK_FUND_TYPE,today+today2 as bu_sum,today,today-lastmonth as lastmonth,today-lastquater as lastquater,today-lastyear as lastyear,
    today2,today2-lastmonth2 as lastmonth2,today2-lastquater2 as lastquater2,today2-lastyear2 as lastyear2
    from(
        select idx,A.SUIK_FUND_TYPE, A.today, A.lastmonth, A.lastquater, A.lastyear,B.today2, B.lastmonth2, B.lastquater2, B.lastyear2
        from(
            select idx, x.SUIK_FUND_TYPE, nvl(a.today,0) today, nvl(b.lastmonth,0) lastmonth,
            nvl(c.lastquater,0) lastquater, nvl(d.lastyear,0) lastyear
            from(
                select rownum as idx, decode(rownum,1,'채권형',2,'주식형',3,'글로벌') SUIK_FUND_TYPE
                from dual connect by level<=3
                ) x,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as today
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.SUIK_FUND_TYPE
                ) a,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.SUIK_FUND_TYPE
                ) b,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05',
                '04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.SUIK_FUND_TYPE
                ) c,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='1본부'
                group by a.SUIK_FUND_TYPE
                ) d
            where x.SUIK_FUND_TYPE=a.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=c.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=d.SUIK_FUND_TYPE(+)
            ) A,
            (
            select decode(x.SUIK_FUND_TYPE,'연기금','NPS','','연기금',x.SUIK_FUND_TYPE) as SUIK_FUND_TYPE, nvl(a.today2,0) today2, nvl(b.lastmonth2,0) lastmonth2,
            nvl(c.lastquater2,0) lastquater2, nvl(d.lastyear2,0) lastyear2
            from(
                select rownum as idx, decode(rownum,1,'채권형',2,'주식형',3,'글로벌') SUIK_FUND_TYPE
                from dual connect by level<=3
                ) x,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) today2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd='{date}' and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.SUIK_FUND_TYPE
                ) a,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastmonth2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.SUIK_FUND_TYPE
                ) b,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastquater2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01','04','04',
                '05','04','06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1) and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.SUIK_FUND_TYPE
                ) c,(
                select a.SUIK_FUND_TYPE,decode(sum(a.suik_set_money),0,0,sum(a.suik_set_money)) as lastyear2
                from SUIKJA_INFO a,FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31') and a.fund_cd<>'1522' and a.suik_mg_bu='2본부'
                group by a.SUIK_FUND_TYPE
                ) d
            where x.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=a.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=c.SUIK_FUND_TYPE(+) and x.SUIK_FUND_TYPE=d.SUIK_FUND_TYPE(+)
            ) B
        where a.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE(+)
        order by idx
        )
    )
group by rollup(SUIK_FUND_TYPE)
"""
    return str


def tab5_win1SearchQuery_old():
    "창 1,2에서 사용"
    str = \
        """    
        /* tab5_win1SearchQuery_old */
        
        select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
        decode(a.INTE_FUND_TYPE,'',decode(b.INTE_FUND_TYPE,'',decode(c.INTE_FUND_TYPE,'',decode(d.INTE_FUND_TYPE,'',e.INTE_FUND_TYPE,d.INTE_FUND_TYPE),c.INTE_FUND_TYPE),b.INTE_FUND_TYPE),a.INTE_FUND_TYPE) INTE_FUND_TYPE,
        nvl(a.suik_set_money,0) as suik_set_money,
        nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY,nvl(b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,nvl(c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
        nvl(d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3, nvl(e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
        nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
        nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
        from(
        select a.tr_ymd,a.suik_name,b.inte_fund_type,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and b.inte_fund_type is not null
        and a.tr_ymd='{date}'and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'
        ) a full outer join (
        select a.tr_ymd,a.suik_name,b.inte_fund_type,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and b.inte_fund_type is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'        
        ) b 
        on  a.SUIK_NAME=b.SUIK_NAME and a.INTE_FUND_TYPE=b.INTE_FUND_TYPE and a.FUND_CD=b.FUND_CD and a.SUIK_SEQ=b.SUIK_SEQ  
        full outer join (
        select a.tr_ymd,a.suik_name,b.inte_fund_type,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and b.inte_fund_type is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
        '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
        and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'        
         ) c
        on a.SUIK_NAME=c.SUIK_NAME and a.INTE_FUND_TYPE=c.INTE_FUND_TYPE and a.FUND_CD=c.FUND_CD and a.SUIK_SEQ=c.SUIK_SEQ
        full outer join (        
        select a.tr_ymd,a.suik_name,b.inte_fund_type,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and b.inte_fund_type is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'       
        ) d
        on a.SUIK_NAME=d.SUIK_NAME and a.INTE_FUND_TYPE=d.INTE_FUND_TYPE and a.FUND_CD=d.FUND_CD and a.SUIK_SEQ=d.SUIK_SEQ 
        full outer join (      
        select a.tr_ymd,a.suik_name,b.inte_fund_type,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and b.inte_fund_type is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'
        ) e
        on a.SUIK_NAME=e.SUIK_NAME and a.INTE_FUND_TYPE=e.INTE_FUND_TYPE and a.FUND_CD=e.FUND_CD and a.SUIK_SEQ=e.SUIK_SEQ
        order by SUIK_NAME, INTE_FUND_TYPE
        """
    return str


def tab5_group1SearchQuery1():
    """inte_fund_type를 SUIK_FUND_TYPE로 기준 고침"""
    str = \
        """    
        /* tab5_group1SearchQuery1 */
        
        select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
        decode(a.SUIK_FUND_TYPE,'',decode(b.SUIK_FUND_TYPE,'',decode(c.SUIK_FUND_TYPE,'',decode(d.SUIK_FUND_TYPE,'',e.SUIK_FUND_TYPE,d.SUIK_FUND_TYPE),c.SUIK_FUND_TYPE),b.SUIK_FUND_TYPE),a.SUIK_FUND_TYPE) SUIK_FUND_TYPE,
        nvl(a.suik_set_money,0) as suik_set_money,nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY, 
        nvl(a.SUIK_NET_MONEY-b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,
        nvl(a.SUIK_NET_MONEY-c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
        nvl(a.SUIK_NET_MONEY-d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3, 
        nvl(a.SUIK_NET_MONEY-e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
        nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
        nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
        from(
        select a.tr_ymd,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd='{date}'and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'
        ) a full outer join (
        select a.tr_ymd,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'        
        ) b 
        on  a.SUIK_NAME=b.SUIK_NAME and a.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE and a.FUND_CD=b.FUND_CD and a.SUIK_SEQ=b.SUIK_SEQ  
        full outer join (
        select a.tr_ymd,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
        '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
        and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'        
         ) c
        on a.SUIK_NAME=c.SUIK_NAME and a.SUIK_FUND_TYPE=c.SUIK_FUND_TYPE and a.FUND_CD=c.FUND_CD and a.SUIK_SEQ=c.SUIK_SEQ
        full outer join (        
        select a.tr_ymd,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'       
        ) d
        on a.SUIK_NAME=d.SUIK_NAME and a.SUIK_FUND_TYPE=d.SUIK_FUND_TYPE and a.FUND_CD=d.FUND_CD and a.SUIK_SEQ=d.SUIK_SEQ 
        full outer join (      
        select a.tr_ymd,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,a.suik_seq,
        decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
        decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
        from SUIKJA_INFO a, FUND_INTEGRATE b
        where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_cd{nps}'PN_NPS' and a.SUIK_FUND_TYPE is not null
        and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')and a.suik_group='{suik_group}' and a.suik_mg_bu='{mg_bu}'
        ) e
        on a.SUIK_NAME=e.SUIK_NAME and a.SUIK_FUND_TYPE=e.SUIK_FUND_TYPE and a.FUND_CD=e.FUND_CD and a.SUIK_SEQ=e.SUIK_SEQ
        order by SUIK_NAME, SUIK_FUND_TYPE
        """
    return str


def tab5_group2SearchQuery1():
    """inte_fund_type를 SUIK_FUND_TYPE로 기준 고침"""
    str = \
        """
    /* tab5_group2SearchQuery1 */
    
    select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
    decode(a.suik_group,'',decode(b.suik_group,'',decode(c.suik_group,'',decode(d.suik_group,'',e.suik_group,d.suik_group),c.suik_group),b.suik_group),a.suik_group) suik_group,
    nvl(a.suik_set_money,0) as suik_set_money,
    nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY,
    nvl(a.SUIK_NET_MONEY-b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,
    nvl(a.SUIK_NET_MONEY-c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
    nvl(a.SUIK_NET_MONEY-d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3,
    nvl(a.SUIK_NET_MONEY-e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
    nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
    nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
    from(
    select a.tr_ymd,a.suik_name,a.suik_group,a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_group is not null
    and a.tr_ymd='{date}'and a.SUIK_FUND_TYPE='{item}' and a.suik_mg_bu='{mg_bu}'
    ) a full outer join (
    select a.tr_ymd,a.suik_name,a.suik_group,a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_group is not null
    and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month)) and a.SUIK_FUND_TYPE='{item}' and a.suik_mg_bu='{mg_bu}'
    ) b
    on  a.SUIK_NAME=b.SUIK_NAME and a.suik_group=b.suik_group and a.FUND_CD=b.FUND_CD and a.SUIK_SEQ=b.SUIK_SEQ
    full outer join (
    select a.tr_ymd,a.suik_name,a.suik_group,a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_group is not null
    and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
    '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
    and a.SUIK_FUND_TYPE='{item}' and a.suik_mg_bu='{mg_bu}'
     ) c
    on a.SUIK_NAME=c.SUIK_NAME and a.suik_group=c.suik_group and a.FUND_CD=c.FUND_CD and a.SUIK_SEQ=c.SUIK_SEQ
    full outer join (
    select a.tr_ymd,a.suik_name,a.suik_group,a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_group is not null
    and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')and a.SUIK_FUND_TYPE='{item}' and a.suik_mg_bu='{mg_bu}'
    ) d
    on a.SUIK_NAME=d.SUIK_NAME and a.suik_group=d.suik_group and a.FUND_CD=d.FUND_CD and a.SUIK_SEQ=d.SUIK_SEQ
    full outer join (
    select a.tr_ymd,a.suik_name,a.suik_group,a.fund_cd,a.suik_seq,
    decode(a.suik_set_money,0,0,a.suik_set_money) as suik_set_money,
    decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000) as suik_net_money
    from SUIKJA_INFO a, FUND_INTEGRATE b
    where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.suik_group is not null
    and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')and a.SUIK_FUND_TYPE='{item}' and a.suik_mg_bu='{mg_bu}'
    ) e
    on a.SUIK_NAME=e.SUIK_NAME and a.suik_group=e.suik_group and a.FUND_CD=e.FUND_CD and a.SUIK_SEQ=e.SUIK_SEQ
    order by SUIK_NAME, suik_group
        """
    return str


def tab5_items1SearchQuery1_old():
    """펀드정보까지 보여주는 조회"""
    str = \
        """
        /* tab5_items1SearchQuery1_old */

        select a.SUIK_NAME,a.suik_group,a.SUIK_FUND_TYPE,a.fund_cd,fund_nm,
        SUIK_NET_MONEY,SUIK_NET_MONEY1,SUIK_NET_MONEY2,SUIK_NET_MONEY3,SUIK_NET_MONEY4,
        suik_set_money1,suik_set_money2,suik_set_money3,suik_set_money4
        from(
            select decode(a.SUIK_NAME,'',decode(b.SUIK_NAME,'',decode(c.SUIK_NAME,'',decode(d.SUIK_NAME,'',e.SUIK_NAME,d.SUIK_NAME),c.SUIK_NAME),b.SUIK_NAME),a.SUIK_NAME) SUIK_NAME,
            decode(a.suik_group,'',decode(b.suik_group,'',decode(c.suik_group,'',decode(d.suik_group,'',e.suik_group,d.suik_group),c.suik_group),b.suik_group),a.suik_group) suik_group,
            decode(a.SUIK_FUND_TYPE,'',decode(b.SUIK_FUND_TYPE,'',decode(c.SUIK_FUND_TYPE,'',decode(d.SUIK_FUND_TYPE,'',e.SUIK_FUND_TYPE,d.SUIK_FUND_TYPE),c.SUIK_FUND_TYPE),b.SUIK_FUND_TYPE),a.SUIK_FUND_TYPE) SUIK_FUND_TYPE,
            decode(a.fund_cd,'',decode(b.fund_cd,'',decode(c.fund_cd,'',decode(d.fund_cd,'',e.fund_cd,d.fund_cd),c.fund_cd),b.fund_cd),a.fund_cd) fund_cd,
            nvl(a.suik_set_money,0) as suik_set_money,nvl(a.SUIK_NET_MONEY,0) as SUIK_NET_MONEY,
            nvl(a.SUIK_NET_MONEY-b.SUIK_NET_MONEY,0) as SUIK_NET_MONEY1,
            nvl(a.SUIK_NET_MONEY-c.SUIK_NET_MONEY,0) as SUIK_NET_MONEY2,
            nvl(a.SUIK_NET_MONEY-d.SUIK_NET_MONEY,0) as SUIK_NET_MONEY3,
            nvl(a.SUIK_NET_MONEY-e.SUIK_NET_MONEY,0) as SUIK_NET_MONEY4,
            nvl(b.suik_set_money,0) as suik_set_money1,nvl(c.suik_set_money,0) as suik_set_money2,
            nvl(d.suik_set_money,0) as suik_set_money3,nvl(e.suik_set_money,0) as suik_set_money4
            from(
                select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
                sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
                sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
                from SUIKJA_INFO a, FUND_INTEGRATE b
                where  a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd='{date}'
                group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
                ) a full outer join (
                select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
                sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
                sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
                from SUIKJA_INFO a, FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,7),'yyyy-mm')-(interval'1'month))
                group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
                ) b
                on  a.SUIK_NAME=b.SUIK_NAME and a.SUIK_FUND_TYPE=b.SUIK_FUND_TYPE and a.FUND_CD=b.FUND_CD
                full outer join (
                select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
                sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
                sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
                from SUIKJA_INFO a, FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=last_day(to_date(substr('{date}',0,4)||decode(substr('{date}',6,2),'01','01','02','01','03','01', '04','04','05','04',
                '06','04', '07','07','08','07','09','07', '10','10','11','10','12','10'),'yyyy/mm')-1)
                group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
                 ) c
                on a.SUIK_NAME=c.SUIK_NAME and a.SUIK_FUND_TYPE=c.SUIK_FUND_TYPE and a.FUND_CD=c.FUND_CD
                full outer join (
                select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
                sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
                sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
                from SUIKJA_INFO a, FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-1||'/12/31')
                group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
                ) d
                on a.SUIK_NAME=d.SUIK_NAME and a.SUIK_FUND_TYPE=d.SUIK_FUND_TYPE and a.FUND_CD=d.FUND_CD
                full outer join (
                select a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd,
                sum(decode(a.suik_set_money,0,0,a.suik_set_money)) as suik_set_money,
                sum(decode(a.suik_set_vol*b.inte_basic_price,0,0,a.suik_set_vol*b.inte_basic_price/1000)) as suik_net_money
                from SUIKJA_INFO a, FUND_INTEGRATE b
                where 1=1 and a.fund_cd=b.fund_cd and a.tr_ymd=b.tr_ymd and a.fund_cd<>'1522' and a.SUIK_FUND_TYPE is not null
                and a.tr_ymd=to_date(substr('{date}',0,4)-2||'/12/31')
                group by a.tr_ymd,a.suik_group,a.suik_name,a.SUIK_FUND_TYPE,a.fund_cd
            ) e
            on a.SUIK_NAME=e.SUIK_NAME and a.SUIK_FUND_TYPE=e.SUIK_FUND_TYPE and a.FUND_CD=e.FUND_CD
            ) a, (
            select FUND_CD,fund_nm,tr_ymd
            from  FUND_BASIC a
            where tr_ymd=(select max(tr_ymd)
                            from FUND_BASIC
                            where a.FUND_CD=FUND_CD)
            ) b
        where a.fund_cd=b.fund_cd
        order by a.FUND_CD, fund_nm


        """
    return str


def tab_hanaSearchQuery():
    """하나펀드에서 보내주는 테이블 위주로 사용시"""
    print("하나펀드")
#     str= \
#         select
#     distinct
#     b.기준일자, a.펀드코드, d.위탁사펀드명
#     , (select listagg(수익자명, ',') as aa
#     from
#     (select 수익자명 from 정보_수익자 f, 펀드_수익자정보 e
#     where a.펀드코드=e.펀드코드(+)
#     and e.수익자코드 = f.수익자코드
#     group
#     by
#     수익자명)) as 수익자명
#     , i.펀드회계유형명,
#     (select 공통코드값명 from 공통코드 where a.집합투자기구2차분류코드=공통코드값 and 공통코드ID='000418') as 펀드유형,
#     (select 공통코드값명 from 공통코드 where a.공모사모코드=공통코드값 and 공통코드ID='000222') as 공모사모구분,
#     '' as 모자구분
#     ,
#     '' as 종류별구분,
#     ''
#     펀드구분,
#     (select 공통코드값명 from 공통코드 where a.적용법령구분코드=공통코드값 and 공통코드ID='000436') as 적용법률,
#     a.자본시장통합법적용일자 as 자통법적용일, a.최초설정일자, a.다음결산일자, a.상환예정일자, a.다음보수인출일자, c.판매회사보수율,
#     c.운용회사보수율, 사무수탁사보수율, 수탁사보수율, 펀드평가회사보수율, ''
#     자산관리보수, ''
#     상품관리보수, 성과보수율, 성과보수여부,
#     round(c.판매회사보수율 + c.운용회사보수율 + 사무수탁사보수율 + 수탁사보수율 + 펀드평가회사보수율, 2) as total,
#     설정금액,
#     ''
#     전일설정좌수, b.총자산 as 전일총자산, b.순자산 as 전일순자산, round(b.원기준가격, 3) as 전일기준가, -- -1
#     영업일
#     계산필요
#     d.위탁사펀드약어명, d.위탁사펀드영문명,
#     (select listagg(운용역명, ', ')
#     from
#     (select h.운용역명 from 정보_운용역담당펀드 m, 운용역코드 h
#     where a.펀드코드=b.펀드코드 and m.펀드코드=a.펀드코드 and m.운용역코드=h.운용역코드
#     group by 운용역명)) as 운용역명,
#     a.운용회사코드 as 운용사,
#     (select 공통코드값명 from 공통코드 where a.수탁사코드=공통코드값 and 공통코드ID='000976') as 수탁사,
#     g.사무수탁사명 as 사무관리사, ''
#     펀드평가사,
#
#
# (select count( *)
# from 펀드_판매사별실적 where
# a.펀드코드 = 펀드코드 and b.기준일자 = 기준일자) as 판매사갯수,
# (select listagg(매매처명, ', ') as aa
# from
#
# (
#     select 펀드판매회사코드, 매매처명 from 펀드_판매사별실적 c, 정보_매매처 d
# where a.펀드코드=c.펀드코드 and b.기준일자=c.기준일자 and c.펀드판매회사코드=매매처코드
# group by 펀드판매회사코드, 매매처명
# )) as 판매사
# , 금융투자협회종목코드 as 협회표준코드, 금융감독원코드 as 금감원코드, 증권예탁원펀드코드 as 예탁원펀드코드, 증권예탁원종목코드 as 예탁원종목코드, 상품분류코드,
# ''
# 상품분류2차,
# 집합투자기구1차분류코드 | | 집합투자기구2차분류코드 | | 집합투자기구3차분류코드 | | 집합투자기구4차분류코드 | | 집합투자기구5차분류코드 | | 집합투자기구6차분류코드 | | 집합투자기구7차분류코드 | | 집합투자기구8차분류코드 | | 집합투자기구9차분류코드 | | 집합투자기구10차분류코드 | |
# 집합투자기구11차분류코드 | | 집합투자기구12차분류코드 | | 집합투자기구13차분류코드 | | 집합투자기구14차분류코드 | | '?' as 집합투자기구분류
# , 펀드결제수수료계상여부,
# (select 공통코드값명 from 공통코드 where a.분배방법구분코드=공통코드값 and 공통코드ID='000221') as 분배방식,
# ''
# 당기결산방식, a.시가평가여부, ''
# 장단기부분, a.국외세액환급여부, ''
# 이관일, ''
# 이수일, ''
# 부사무관리사, a.해외주식비과표대상여부, a.해외주식비과표적용일자, ''
# 설정대금확정일1, ''
# 설정일,
# ''
# 환매대금확정일1, ''
# 환매일1, ''
# 환매대금확정일2, ''
# 환매일2, ''
# 위탁사자체유형, ''
# 펀드결제수수료면제시작일, ''
# 펀드결제수수료종료일, ''
# 펀드결제수수료유예시작일, ''
# 펀드결제수수료유예종료일, ''
# 채권평가사보수유예시작일, ''
# 채권평가사보수유예종료일,
# 수탁사코드, ''
# 배당기준운용사,
# ''
# 신주인수권증서평가기준_폐지일,
# ''
# 공모청약수수료기준,
# ''
# 단위형구분, ''
# 수익차등여부,
# (select 공통코드값명 from 공통코드 where a.사모구분코드=공통코드값 and 공통코드ID='001015') as 사모분류,
# ''
# 일반투자자포함여부
# from 펀드_마스터 a, 펀드_기준가격
#
# b, 펀드_보수율
# c, 펀드_위탁사별펀드정보
# d, 정보_사무수탁사
# g, 정보_펀드회계유형
# i, 펀드_보수계산정보
# l, 정보_운용역담당펀드
# m, 운용역코드
# h
# where
# a.펀드코드 = b.펀드코드
# and a.펀드코드 = c.펀드코드
# and a.펀드코드 = d.펀드코드
# and a.사무수탁사코드 = g.사무수탁사코드
# and a.펀드회계유형코드 = i.펀드회계유형코드
# and m.운용역코드 = h.운용역코드
# and a.펀드코드 = m.펀드코드
# and c.유효시작일자 <= '2021/11/09'
# and c.유효종료일자 >= '2021/11/09'
# and b.기준일자 >= '2021/11/09'
# and a.펀드코드 = 'ER11'
# order
# by
# 펀드코드
# asc;