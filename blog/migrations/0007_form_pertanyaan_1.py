# Generated by Django 4.2.3 on 2023-09-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_form_quetion1_remove_form_quetion2'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='pertanyaan_1',
            field=models.CharField(choices=[['a.expend energy, enjoy groups or', 'b.conserve energy, enjoy one-on-one'], ['a.more outgoing, think out loud or', 'b.more reserved, think to yourself'], ['a.seek many tasks, public activities, interaction with others', 'b.seek private, solitary activities with quiet to concentrate'], ['a.external, communicative, express yourself or', 'b.internal, reticent, keep to yourself'], ['a.active, initiate or', 'b.reflective, deliberate'], ['a.interpret literally or', 'b.look for meaning and possibilities'], ['a.practical, realistic, experiential or', 'b.imaginative, innovative, theoretical'], ['a.standard, usual, conventional or', 'b.different, novel, unique'], ['a.focus on here-and-now or', 'b.look to the future, global perspective, “big picture”'], ['a.facts, things, “what is” or', 'b.ideas, dreams, “what could be,” philosophical'], ['a.logical, thinking, questioning or', 'b.empathetic, feeling, accommodating'], ['a. candid, straight forward, frank or', 'b. tactful, kind, encouraging'], ['a.firm, tend to criticize, hold the line or', 'b.gentle, tend to appreciate, conciliate'], ['a.tough-minded, just or', 'b.tender-hearted, merciful'], ['a.matter of fact, issue-oriented or', 'b.sensitive, people-oriented, compassionate'], ['a. organized, orderly or', 'b. flexible, adaptable'], ['a. plan, schedule or', 'b. unplanned, spontaneous'], ['a.regulated, structured or', 'b.easygoing, “live” and “let live”'], ['a.preparation, plan ahead or', 'b.go with the flow, adapt as you go'], ['a.control, govern or', 'b.latitude, freedom']], default=1, max_length=128),
            preserve_default=False,
        ),
    ]
