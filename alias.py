import os

cmd = os.system

# Terminal alias
alias = "" \
        "# NightFox Alias" \
        "alias ..='clear'" \
        "alias ll='ls -AFCX'" \
        "alias lm='echo;lm -l;echo;pwd;echo;'" \
        "alias py='python3'" \
        "alias srv='service --status-all'" \
        "alias srx='service --status-all | grep "+"'" \
        "alias q='exit'" \
        ""

# creat payload file in /tmp (leave no lead in tmp)
# echo 'alias' > /tmp/alias.sh

# /root/.bashrc
# /home/$USER/.bashrc

cmd(f'echo {alias} > ./a.txt')
