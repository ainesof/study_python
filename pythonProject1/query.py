def returnSQL(para):
    if para == 'tab3_win1SearchQuery':
        sql = tab3_win1SearchQuery()
    elif para == 'tab3_SearchQuery':
        sql = tab3_SearchQuery()

    return sql


# 펀드구조구분코드 IN ('01','02','04','06')--일반펀드,모펀드,클래스운용,클래스운용(자)
# 펀드구조구분코드 IN ('01','03','04','06')--일반펀드,자펀드,클래스운용,클래스운용(자)
# 펀드구조구분코드 IN ('01','02','04')     --일반펀드,모펀드,클래스운용

def tab3_SearchQuery():
    """탭3 메인부분"""
    str = \
        "select b.tr_ymd as 기준일, a.펀드코드, b.fund_full_nm, " \
        "(select 공통코드값명 from 공통코드 where b.fund_sintak_mm=공통코드값 and 공통코드ID='001049')수익자구분, " \
        "   (select listagg(수익자명, ',') from (select 수익자명 from 정보_수익자 f, 펀드_수익자정보 e where a.펀드코드=e.펀드코드(+) and e.수익자코드=f.수익자코드 group by 수익자명)) as 수익자, " \
        " (select 펀드회계유형명 from 정보_펀드회계유형 where a.펀드회계유형코드=펀드회계유형코드) as 펀드종류구분, b.fund_type as 펀드유형, '?'일임자문, b.fund_gongmo_samo as 공모사모구분, b.fund_in_foreign as 국내해외, b.fund_moja_gu as 모자구분, " \
        "  case when a.펀드구조구분코드='04' then '클래스운용펀드' when a.펀드구조구분코드='05' then '클래스펀드' when a.펀드구조구분코드='06' then '클래스운용펀드' else '' end as 종류형구분,  '?' as 펀드구분, " \
        " (select 공통코드값명 from 공통코드 where a.적용법령구분코드=공통코드값 and 공통코드ID='000436') as 적용법률, a.자본시장통합법적용일자 as 자통법적용일, a.최초설정일자, " \
        " (select min(tr_ymd) from FUND_INTEGRATE where a.펀드코드=FUND_CD) as 운용개시일, " \
        "a.다음결산일자,a.상환예정일자 as 상환일,a.다음보수인출일자, " \
        "round(b.FUND_PANMEBOSU_BP,2) as 판매보수,round(b.FUND_MANBOSU_BP,2) as 운용보수,round(b.FUND_SAMUBOSU_BP,2) as 사무관리보수,round(b.FUND_SUTAKBOSU_BP,2) as 수탁보수,round(b.FUND_EVALBOSU_BP,2) as 펀드평가보수, " \
        "round(b.FUND_JAMUNBOSU_BP,2) as 자산관리보수,'?'상품관리보수,round(b.FUND_ADDBOSU_BP,2) as 성과보수율,a.성과보수여부, " \
        " round(b.FUND_PANMEBOSU_BP,2)+round(b.FUND_MANBOSU_BP,2)+round(b.FUND_SAMUBOSU_BP,2)+round(b.FUND_SUTAKBOSU_BP,2)+round(b.FUND_EVALBOSU_BP,2)+nvl(round(b.FUND_JAMUNBOSU_BP,2),0)+nvl(round(b.FUND_ADDBOSU_BP,2),0) as total," \
        "  to_char(c.INTE_SET_VOL, '999,999,999,999,999') as 설정액, to_char(c.INTE_ORIGIN_MONEY, '999,999,999,999,999') as 설정좌수, to_char(b.FUND_TOT_JASAN, '999,999,999,999,999') as 총자산, " \
        " to_char(round(c.INTE_NET_MONEY_AF,2), '999,999,999,999,999') as 순자산,to_char(round(e.OPER_RAT_PRICE), '999,999,999,999,999') as 기준가,'?'누적수익지수,b.fund_nm as 펀드약명, " \
        "b.fund_eng_full_nm as 영문명,c.inte_man 운용역,(select 공통코드값명 from 공통코드 where a.운용회사코드=공통코드값정의 and 공통코드ID='001128') as 운용사명,b.fund_sutak_nm as 수탁은행,'?'수탁사명, b.fund_samusutak_nm as 사무수탁사명,b.fund_pungsa_nm as 펀드평가사, " \
        "(select count(*) from FUND_COMPANY x where a.펀드코드=x.fund_cd and b.tr_ymd=x.tr_ymd) as 판매사갯수, " \
        "(select listagg(comp_sale_nm,', ') from(select x.fund_cd,x.comp_sale_nm from  FUND_COMPANY x where a.펀드코드=x.fund_cd and b.tr_ymd=x.tr_ymd)) as 판매사, " \
        "금융투자협회종목코드 as 협회표준코드,금융감독원코드 as 금감원코드,증권예탁원펀드코드 as 예탁원펀드코드,증권예탁원종목코드 as 예탁원종목코드,a.상품분류코드,'?'상품분류2차, " \
        "집합투자기구1차분류코드||집합투자기구2차분류코드||집합투자기구3차분류코드||집합투자기구4차분류코드||집합투자기구5차분류코드||집합투자기구6차분류코드||집합투자기구7차분류코드||집합투자기구8차분류코드||집합투자기구9차분류코드||집합투자기구10차분류코드||  " \
        "집합투자기구11차분류코드||집합투자기구12차분류코드||집합투자기구13차분류코드||집합투자기구14차분류코드 as 집합투자기구구분, " \
        "a.펀드결제수수료계상여부 as 펀드결제수수료여부, " \
        "(select 공통코드값명 from 공통코드 where a.분배방법구분코드=공통코드값 and 공통코드ID='000221') as 분배방식, " \
        "(select 공통코드값명 from 공통코드 where a.분배방법구분코드=공통코드값 and 공통코드ID='000221') as 당기결산방식,a.시가평가여부,'?'장단기부분,a.국외세액환급여부,'?'이관일,d.유효시작일자 as 이수일,'?'투자자,(select 공통코드값정의 from 공통코드 where a.부사무관리펀드코드=공통코드값 and 공통코드ID='001030') as 부사무관리사,a.해외주식비과표대상여부,a.해외주식비과표적용일자,'?'설정대금확정일1,'?'설정일1, " \
        "'?'환매대금확정일1,'?'환매일1,'?'환매대금확정일2,'?'환매일2,e.oper_bm_way as BM명,'?'GIPS펀드유형,'?'채권평가사보수유예시작일,'?'채권평가사보수유예종료일,'?'배당기준운용사,'?'신주인수권증서평가기준_폐지일,'?'공모청약수수료기준,b.fund_danwi_gu as 단위형구분,'?'수익차등여부, " \
        "(select 공통코드값명 from 공통코드 where a.사모구분코드=공통코드값 and 공통코드ID='001015') as 사모분류, '?'일반투자자포함여부 " \
        "from 펀드_마스터 a, FUND_BASIC b, FUND_INTEGRATE c, 펀드_운용회사변경내역 d, FUND_OPERATE e " \
        "where a.펀드코드=b.fund_cd " \
        "and a.펀드코드=c.fund_cd " \
        "and a.펀드코드 = e.fund_cd " \
        "and b.tr_ymd = e.tr_ymd " \
        "and a.펀드코드=d.펀드코드(+) " \
        "and b.tr_ymd=c.tr_ymd "

    return str


def tab3_win1SearchQuery():
    """탭3 새창 더블클릭시 내용읽는 부분"""
    str = \
        "select a.TR_YMD,b.inte_modi_price, " \
        "nvl(b.inte_modi_price - lead(b.inte_modi_price) over (order by a.TR_YMD desc),0) a, " \
        "a.FUND_SET_MONEY,a.FUND_SET_VOL, " \
        "c.당일설정좌수,c.당일해지좌수,nvl(a.FUND_SET_VOL - lead(a.FUND_SET_VOL) over (order by a.TR_YMD desc),0) as aa, " \
        "a.FUND_TOT_JASAN, nvl(a.FUND_TOT_JASAN - lead(a.FUND_TOT_JASAN) over (order by a.TR_YMD desc),0) b, " \
        "a.FUND_NET_JASAN, nvl(a.FUND_NET_JASAN - lead(a.FUND_NET_JASAN) over (order by a.TR_YMD desc),0) c   " \
        "from FUND_BASIC a, FUND_INTEGRATE b, 펀드_설정해지원장 c " \
        "where b.fund_cd=a.fund_cd and a.TR_YMD=b.TR_YMD  and b.fund_cd=c.펀드코드 and a.tr_ymd=c.기준일자 "
    return str


def tab_searchValue():
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