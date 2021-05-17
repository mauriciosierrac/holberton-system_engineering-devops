# 0x19. Postmortem


![Hbnb](https://github.com/mauriciosierrac/holberton-system_engineering-devops/blob/master/0x19-postmortem/antiransomware.jpg)

## Resources:books:
Read or watch:
* [Incident Report, also referred to as a Postmortem](https://intranet.hbtn.io/rltoken/QTu2_ZVW8f-2weQGOQvc9w)
* [How to run a Postmortem](https://intranet.hbtn.io/rltoken/uost5-f-wlp7CV2a6OLVKQ)

---
## Issue Summary

Cervalle S.A. users began to report connection problems with the accounting program database and production software, others reported that they could not access shared network resources, and local files on the computers were also reported to be inaccessible.


## Timeline

 * 8:00am invoicing users reported a problem accessing the program and were unable to create invoices.
 * 8:15am users in accounting and other areas report that they are unable to access network resources.
 * 8:30am it was detected that the database configuration files on the database server were encrypted, as were many other files on the network.
 * 8:35am the network is disabled and a full scan of the network is performed, looking for possible foreign processes running.
 * 9:00am it is detected that the company is under attack by a virus called Ransomeware, which encrypts different files on the network and leaves an html message with payment instructions, it was a kidnapping of information.
 * 9:20am an attempt is made to fix the problem with the antivirus network agent.
 * 9:40am When we contacted the support line of the McAffee antivirus service, we found out that this type of virus still has no solution and that for now we have to pay to recover the information.
 * 10:00am With the information provided by the McAffe support line, we decided that the best thing to do was to restore the backup that had been made at midnight on the day in question.
 * 10:15am the backup restore is completed and users can access the system again.
 * 10:40 am network logs are reviewed to identify unusual network traffic and to determine the source of the attack.
 * 1:00pm the virus was detected entering the network through an attachment in an e-mail.


## Root Cause

The ransomware virus is a type of virus that enters a network through a web link, installs backdoors and begins to download little by little, once it is complete it is executed by performing a scan on the network, is copied to each network drive connected to the zoombie computer and multiplies over the network, encrypting all files with Microsoft office extensions, images, pdf, backup files, rar files, among others.
It uses an extremely advanced encryption algorithm that so far has no known solution.


## Correct and Preventative Measures

when we learned that the encryption algorithm is inviolable without the key, we decided to restore the backups immediately prior to the event to give access as soon as possible to users and resume activities again, as a preventive measure, a socialization campaign will be conducted with the staff so that they know the new ways in which hackers act and how to identify a possible attack.
in the same way, more security copies will be configured in the database server in order to have more options and a network monitoring agent will be installed to identify any strange traffic.




---

## Author
* **Mauricio Sierra Cifuentes** - [mauriciosierrac](https://github.com/mauriciosierrac)