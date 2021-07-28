@EventHandler
public void onDeath(PlayerDeathEvent e){
	ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":skull: "+e.getEntity().getName()+" IS DEAD.").queue();
	ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":skull: Reason: "+e.getDeathMessage()).queue();
}

@EventHandler
public void theDiamonds(PlayerAdvancementDoneEvent e){
	if(e.getAdvancement().getKey().getKey().equals("story/mine_diamond")){
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":large_blue_diamond: "+e.getPlayer().getName()+" got diamonds!!!!!!!!!!").queue();
	}
}

@EventHandler
public void theNether(PlayerAdvancementDoneEvent e){
	if(e.getAdvancement().getKey().getKey().equals("story/enter_the_nether")){
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":japanese_goblin: "+e.getPlayer().getName()+" goes in the Nether for the first time.....").queue();
	}
}

@EventHandler
public void theEnd(PlayerAdvancementDoneEvent e){
	if(e.getAdvancement().getKey().getKey().equals("story/enter_the_end")){
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":dragon_face: "+e.getPlayer().getName()+" goes in the END...").queue();
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":crossed_swords: GOGOGO THIS DRAGON WILL BE DEAD :crossed_swords:").queue();
	}
}

@EventHandler
public void theDragonDied(PlayerAdvancementDoneEvent e){
	if(e.getAdvancement().getKey().getKey().equals("end/kill_dragon")){
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":sunglasses: "+e.getPlayer().getName()+" killed the dragon :sunglasses:").queue();
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":heart: The server is proud of you :heart:").queue();
	}
}


@EventHandler
public void theSurvivor(PlayerAdvancementDoneEvent e){
	if(e.getAdvancement().getKey().getKey().equals("adventure/totem_of_undying")){
		ScriptBot.getBot().getTextChannelById("XXXXXXXXXXXXXXXXXX").sendMessage(":sweat_smile: "+e.getPlayer().getName()+" managed to not delete this seed!!!!!!!!").queue();
	}
}
