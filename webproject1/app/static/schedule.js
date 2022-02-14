function schedule_set(){
<!-- 24시간 기준 00:00형식 시간, 함수명, 설명 순 -->
    const task=[['11:19','test1()','테스트1'],
                ['11:18','test2()','테스트2'],
                ['13:08','kfr_getfile()','FTP자료 다운']];
    var comment='';
    for(var i=0;i<task.length;i++){
        comment=comment+task[i][0]+' '+task[i][2]+'\n';
    }

    $('#scheduler_do').attr('title','대기 중인 스케쥴:\n'+comment);

    if(schdule_status=='open'){
        var nowHour = String(new Date().getHours()).padStart(2,'0');
        var nowMin = String(new Date().getMinutes()).padStart(2,'0');
        var nowSec = String(new Date().getSeconds()).padStart(2,'0');
        var nowtime = nowHour + ":" + nowMin;
        $('#scheduler_do').html('스케쥴러 '+nowtime+ ":" + nowSec);

        if(nowSec=='00'){
            for(var i=0;i<task.length;i++){
                if(task[i][0]==nowtime) eval(task[i][1]);
            }
        }
    }
}

function test1(){ $('.modal').fadeIn(); }
function test2(){ $('.modal').fadeIn(); }

