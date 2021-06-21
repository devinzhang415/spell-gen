"""
DnD 5e program to randomize the spells of your wizard enemies by Devin Zhang 6/20/21 - 6/21/21
"""

import numpy
import math
import random

class Spell():
    def __init__(self, name, level, school):
        self.name = name
        self.level = level
        self.school = school

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level

    def get_school(self):
        return self.school

def gen_weights(spells, level, school = ""):
    weights = []
    for spell in spells:
        if spell.get_level() == level and spell.get_school() == school:
            weights.append(3.5)
        elif spell.get_level() == level:
            weights.append(1.0)
        else:
            weights.append(0.0)
    weights = numpy.array(weights)
    weights /= weights.sum()
    return weights

def gen_spells(num, spells, weights):
    return numpy.random.choice(spells, num, False, weights)

def main():
    acid_splash = Spell("acid splash", 0, "conjuration")
    chill_touch = Spell("chill touch", 0, "necromancy")
    dancing_lights = Spell("dancing lights", 0, "evocation")
    fire_bolt = Spell("fire bolt", 0, "evocation")
    light = Spell("light", 0, "evocation")
    mage_hand = Spell("mage hand", 0, "conjuration")
    mending = Spell("mending", 0, "transmutation")
    message = Spell("message", 0, "transmutation")
    minor_illusion = Spell("minor illusion", 0, "illusion")
    poison_spray = Spell("poison spray", 0, "conjuration")
    prestidigitation = Spell("prestidigitation", 0, "transmutation")
    ray_of_frost = Spell("ray of frost", 0, "evocation")
    shocking_grasp = Spell("shocking grasp", 0, "evocation")
    true_strike = Spell("true strike", 0, "divination")
    alarm = Spell("alarm", 1, "abjuration")
    burning_hands = Spell("burning hands", 1, "evocation")
    charm_person = Spell("charm person", 1, "enchantment")
    color_spray = Spell("color spray", 1, "illusion")
    comprehend_languages = Spell("comprehend languages", 1, "divination")
    detect_magic = Spell("detect magic", 1, "divination")
    disguise_self = Spell("disguise self", 1, "illusion")
    expeditious_retreat = Spell("expeditious retreat", 1, "transmutation")
    false_life = Spell("false life", 1, "necromancy")
    feather_fall = Spell("feather fall", 1, "transmutation")
    find_familiar = Spell("find familiar", 1, "conjuration")
    fog_cloud = Spell("fog cloud", 1, "conjuration")
    grease = Spell("grease", 1, "conjuration")
    identify = Spell("identify", 1, "divination")
    illusory_script = Spell("illusory script", 1, "illusion")
    jump = Spell("jump", 1, "transmutation")
    longstrider = Spell("longstrider", 1, "transmutation")
    mage_armor = Spell("mage armor", 1, "abjuration")
    magic_missile = Spell("magic missile", 1, "evocation")
    protection_from_evil_and_good = Spell("protection from evil and good", 1, "abjuration")
    shield = Spell("shield", 1, "abjuration")
    silent_image = Spell("silent image", 1, "illusion")
    sleep = Spell("sleep", 1, "enchantment")
    tashas_hideous_laughter = Spell("Tasha's hideous laughter", 1, "enchantment")
    tensers_floating_disk = Spell("Tenser's floating disk", 1, "conjuration")
    thunderwave = Spell("thunderwave", 1, "evocation")
    unseen_servant = Spell("unseen servant", 1, "conjuration")
    alter_self = Spell("alter self", 2, "transmutation")
    arcane_lock = Spell("arcane lock", 2, "abjuration")
    augury = Spell("augury", 2, "divination")
    blindness_deafness = Spell("blindness/deafness", 2, "necromancy")
    blur = Spell("blur", 2, "illusion")
    continual_flame = Spell("continual flame", 2, "evocation")
    darkness = Spell("darkness", 2, "evocation")
    darkvision = Spell("darkvision", 2, "transmutation")
    detect_thoughts = Spell("detect thoughts", 2, "divination")
    enhance_ability = Spell("enhance ability", 2, "transmutation")
    enlarge_reduce = Spell("enlarge/reduce", 2, "transmutation")
    flaming_sphere = Spell("flaming sphere", 2, "conjuration")
    gentle_repose = Spell("gentle repose", 2, "necromancy")
    gust_of_wind = Spell("gust of wind", 2, "evocation")
    hold_person = Spell("hold person", 2, "enchantment")
    invisibility = Spell("invisibility", 2, "illusion")
    knock = Spell("knock", 2, "transmutation")
    levitate = Spell("levitate", 2, "transmutation")
    locate_object = Spell("locate object", 2, "divination")
    magic_mouth = Spell("magic mouth", 2, "illusion")
    magic_weapon = Spell("magic weapon", 2, "transmutation")
    melfs_acid_arrow = Spell("Melf's acid arrow", 2, "evocation")
    mirror_image = Spell("mirror image", 2, "illusion")
    misty_step = Spell("misty step", 2, "conjuration")
    nystuls_magic_aura = Spell("Nystul's magic aura", 2, "illusion")
    ray_of_enfeeblement = Spell("ray of enfeeblement", 2, "necromancy")
    rope_trick = Spell("rope trick", 2, "transmutation")
    scorching_ray = Spell("scorching ray", 2, "evocation")
    see_invisibility = Spell("see invisibility", 2, "divination")
    shatter = Spell("shatter", 2, "evocation")
    spider_climb = Spell("spider climb", 2, "transmutation")
    suggestion = Spell("suggestion", 2, "enchantment")
    web = Spell("web", 2, "conjuration")
    animate_dead = Spell("animate dead", 3, "necromancy")
    bestow_curse = Spell("bestow curse", 3, "necromancy")
    blink = Spell("blink", 3, "transmutation")
    clairvoyance = Spell("clairvoyance", 3, "divination")
    counterspell = Spell("counterspell", 3, "abjuration")
    dispel_magic = Spell("dispel magic", 3, "abjuration")
    fear = Spell("fear", 3, "illusion")
    fireball = Spell("fireball", 3, "evocation")
    fly = Spell("fly", 3, "transmutation")
    gaseous_form = Spell("gaseous form", 3, "transmutation")
    glyph_of_warding = Spell("glyph of warding", 3, "abjuration")
    haste = Spell("haste", 3, "transmutation")
    hypnotic_pattern = Spell("hypnotic pattern", 3, "illusion")
    leomunds_tiny_hut = Spell("Leomund's tiny hut", 3, "evocation")
    lightning_bolt = Spell("lightning bolt", 3, "evocation")
    magic_circle = Spell("magic circle", 3, "abjuration")
    major_image = Spell("major image", 3, "illusion")
    nondetection = Spell("nondetection", 3, "abjuration")
    phantom_steed = Spell("phantom steed", 3, "illusion")
    protection_from_energy = Spell("protection from energy", 3, "abjuration")
    remove_curse = Spell("remove curse", 3, "abjuration")
    sending = Spell("sending", 3, "evocation")
    sleet_storm = Spell("sleet storm", 3, "conjuration")
    slow = Spell("slow", 3, "transmutation")
    speak_with_dead = Spell("speak with dead", 3, "necromancy")
    stinking_cloud = Spell("stinking cloud", 3, "conjuration")
    tongues = Spell("tongues", 3, "divination")
    vampiric_touch = Spell("vampiric touch", 3, "necromancy")
    water_breathing = Spell("water breathing", 3, "transmutation")
    arcane_eye = Spell("arcane eye", 4, "divination")
    banishment = Spell("banishment", 4, "abjuration")
    blight = Spell("blight", 4, "necromancy")
    confusion = Spell("confusion", 4, "enchantment")
    conjure_minor_elementals = Spell("conjure minor elementals", 4, "conjuration")
    control_water = Spell("control water", 4, "transmutation")
    dimension_door = Spell("dimension door", 4, "conjuration")
    divination = Spell("divination", 4, "divination")
    evards_black_tentacles = Spell("Evard's black tentacles", 4, "conjuration")
    fabricate = Spell("fabricate", 4, "transmutation")
    fire_shield = Spell("fire shield", 4, "evocation")
    greater_invisibility = Spell("greater invisibility", 4, "illusion")
    hallucinatory_terrain = Spell("hallucinatory terrain", 4, "illusion")
    ice_storm = Spell("ice storm", 4, "evocation")
    leomunds_secret_chest = Spell("Leomund's secret chest", 4, "conjuration")
    locate_creature = Spell("locate creature", 4, "divination")
    mordenkainens_faithful_hound = Spell("Mordenkainen's faithful hound", 4, "conjuration")
    mordenkainens_private_sanctum = Spell("Mordenkainen's private sanctum", 4, "abjuration")
    otilukes_resilient_sphere = Spell("Otiluke's resilient sphere", 4, "evocation")
    phantasmal_killer = Spell("phantasmal killer", 4, "illusion")
    polymorph = Spell("polymorph", 4, "transmutation")
    stone_shape = Spell("stone shape", 4, "transmutation")
    stoneskin = Spell("stoneskin", 4, "abjuration")
    wall_of_fire = Spell("wall of fire", 4, "evocation")
    animate_objects = Spell("animate objects", 5, "transmutation")
    bigbys_hand = Spell("Bigby's hand", 5, "evocation")
    cloudkill = Spell("cloudkill", 5, "conjuration")
    cone_of_cold = Spell("cone of cold", 5, "evocation")
    conjure_elemental = Spell("conjure elemental", 5, "conjuration")
    contact_other_plane = Spell("contact other plane", 5, "divination")
    creation = Spell("creation", 5, "illusion")
    dominate_person = Spell("dominate person", 5, "enchantment")
    dream = Spell("dream", 5, "illusion")
    geas = Spell("geas", 5, "enchantment")
    hold_monster = Spell("hold monster", 5, "enchantment")
    legend_lore = Spell("legend lore", 5, "divination")
    mislead = Spell("mislead", 5, "illusion")
    modify_memory = Spell("modify memory", 5, "enchantment")
    passwall = Spell("passwall", 5, "transmutation")
    planar_binding = Spell("planar binding", 5, "abjuration")
    rarys_telepathic_bond = Spell("Rary's telepathic bond", 5, "divination")
    scrying = Spell("scrying", 5, "divination")
    seeming = Spell("seeming", 5, "illusion")
    telekinesis = Spell("telekinesis", 5, "transmutation")
    teleportation_circle = Spell("teleportation circle", 5, "conjuration")
    wall_of_force = Spell("wall of force", 5, "evocation")
    wall_of_stone = Spell("wall of stone", 5, "evocation")
    chain_lightning = Spell("chain lightning", 6, "evocation")
    circle_of_death = Spell("circle of death", 6, "necromancy")
    contingency = Spell("contingency", 6, "evocation")
    create_undead = Spell("create undead", 6, "necromancy")
    disintegrate = Spell("disintegrate", 6, "transmutation")
    drawmijs_instant_summons = Spell("Drawmij's instant summons", 6, "conjuration")
    eyebite = Spell("eyebite", 6, "necromancy")
    flesh_to_stone = Spell("flesh to stone", 6, "transmutation")
    globe_of_invulnerability = Spell("globe of invulnerability", 6, "abjuration")
    guards_and_wards = Spell("guards and wards", 6, "abjuration")
    magic_jar = Spell("magic jar", 6, "necromancy")
    mass_suggestion = Spell("mass suggestion", 6, "enchantment")
    move_earth = Spell("move earth", 6, "transmutation")
    otilukes_freezing_sphere = Spell("Otiluke's freezing sphere", 6, "evocation")
    ottos_irresistible_dance = Spell("Otto's irresistible dance", 6, "enchantment")
    programmed_illusion = Spell("programmed illusion", 6, "illusion")
    sunbeam = Spell("sunbeam", 6, "evocation")
    true_seeing = Spell("true seeing", 6, "divination")
    wall_of_ice = Spell("wall of ice", 6, "evocation")
    delayed_blast_fireball = Spell("delayed blast fireball", 7, "evocation")
    etherealness = Spell("etherealness", 7, "transmutation")
    finger_of_death = Spell("finger of death", 7, "necromancy")
    forcecage = Spell("forcecage", 7, "evocation")
    mirage_arcane = Spell("mirage arcane", 7, "illusion")
    mordenkainens_magnificent_mansion = Spell("Mordenkainen's magnificent mansion", 7, "conjuration")
    mordenkainens_sword = Spell("Mordenkainen's sword", 7, "evocation")
    plane_shift = Spell("plane shift", 7, "conjuration")
    prismatic_spray = Spell("prismatic spray", 7, "evocation")
    project_image = Spell("project image", 7, "illusion")
    reverse_gravity = Spell("reverse gravity", 7, "transmutation")
    sequester = Spell("sequester", 7, "transmutation")
    simulacrum = Spell("simulacrum", 7, "illusion")
    symbol = Spell("symbol", 7, "abjuration")
    teleport = Spell("teleport", 7, "conjuration")
    antimagic_field = Spell("antimagic field", 8, "abjuration")
    antipathy_sympathy = Spell("antipathy/sympathy", 8, "enchantment")
    clone = Spell("clone", 8, "necromancy")
    control_weather = Spell("control weather", 8, "transmutation")
    demiplane = Spell("demiplane", 8, "conjuration")
    dominate_monster = Spell("dominate monster", 8, "enchantment")
    feeblemind = Spell("feeblemind", 8, "enchantment")
    incendiary_cloud = Spell("incendiary cloud", 8, "conjuration")
    maze = Spell("maze", 8, "conjuration")
    mind_blank = Spell("mind blank", 8, "abjuration")
    power_word_stun = Spell("power word stun", 8, "enchantment")
    sunburst = Spell("sunburst", 8, "evocation")
    astral_projection = Spell("astral projection", 9, "necromancy")
    foresight = Spell("foresight", 9, "divination")
    gate = Spell("gate", 9, "conjuration")
    imprisonment = Spell("imprisonment", 9, "abjuration")
    meteor_swarm = Spell("meteor swarm", 9, "evocation")
    power_word_kill = Spell("power word kill", 9, "enchantment")
    prismatic_wall = Spell("prismatic wall", 9, "abjuration")
    shapechange = Spell("shapechange", 9, "transmutation")
    time_stop = Spell("time stop", 9, "transmutation")
    true_polymorph = Spell("true polymorph", 9, "transmutation")
    weird = Spell("weird", 9, "illusion")
    wish = Spell("wish", 9, "conjuration")

    spells = [acid_splash,chill_touch,dancing_lights,fire_bolt,light,mage_hand,mending,message,minor_illusion,poison_spray,
                prestidigitation,ray_of_frost,shocking_grasp,true_strike,alarm,burning_hands,charm_person,color_spray,
                comprehend_languages,detect_magic,disguise_self,expeditious_retreat,false_life,feather_fall,find_familiar,
                fog_cloud,grease,identify,illusory_script,jump,longstrider,mage_armor,magic_missile,
                protection_from_evil_and_good,shield,silent_image,sleep,tashas_hideous_laughter,
                tensers_floating_disk,thunderwave,unseen_servant,alter_self,arcane_lock,augury,blindness_deafness,
                blur,continual_flame,darkness,darkvision,detect_thoughts,enhance_ability,enlarge_reduce,flaming_sphere,
                gentle_repose,gust_of_wind,hold_person,invisibility,knock,levitate,locate_object,magic_mouth,magic_weapon,
                melfs_acid_arrow,mirror_image,misty_step,nystuls_magic_aura,ray_of_enfeeblement,rope_trick,scorching_ray,
                see_invisibility,shatter,spider_climb,suggestion,web,animate_dead,bestow_curse,blink,clairvoyance,
                counterspell,dispel_magic,fear,fireball,fly,gaseous_form,glyph_of_warding,haste,hypnotic_pattern,
                leomunds_tiny_hut,lightning_bolt,magic_circle,major_image,nondetection,phantom_steed,protection_from_energy,
                remove_curse,sending,sleet_storm,slow,speak_with_dead,stinking_cloud,tongues,vampiric_touch,water_breathing,
                arcane_eye,banishment,blight,confusion,conjure_minor_elementals,control_water,dimension_door,divination,
                evards_black_tentacles,fabricate,fire_shield,greater_invisibility,hallucinatory_terrain,ice_storm,leomunds_secret_chest,
                locate_creature,mordenkainens_faithful_hound,mordenkainens_private_sanctum,otilukes_resilient_sphere,phantasmal_killer,
                polymorph,stone_shape,stoneskin,wall_of_fire,animate_objects,bigbys_hand,cloudkill,cone_of_cold,conjure_elemental,
                contact_other_plane,creation,dominate_person,dream,geas,hold_monster,legend_lore,mislead,modify_memory,passwall,
                planar_binding,rarys_telepathic_bond,scrying,seeming,telekinesis,teleportation_circle,wall_of_force,wall_of_stone,
                chain_lightning,circle_of_death,contingency,create_undead,disintegrate,drawmijs_instant_summons,eyebite,flesh_to_stone,
                globe_of_invulnerability,guards_and_wards,magic_jar,mass_suggestion,move_earth,otilukes_freezing_sphere,
                ottos_irresistible_dance,programmed_illusion,sunbeam,true_seeing,wall_of_ice,delayed_blast_fireball,etherealness,
                finger_of_death,forcecage,mirage_arcane,mordenkainens_magnificent_mansion,mordenkainens_sword,plane_shift,prismatic_spray,
                project_image,reverse_gravity,sequester,simulacrum,symbol,teleport,antimagic_field,antipathy_sympathy,clone,
                control_weather,demiplane,dominate_monster,feeblemind,incendiary_cloud,maze,mind_blank,power_word_stun,
                sunburst,astral_projection,foresight,gate,imprisonment,meteor_swarm,power_word_kill,prismatic_wall,shapechange,
                time_stop,true_polymorph,weird,wish]

    spell_slots = {
        1:  [3,2],
        2:  [3,3],
        3:  [3,4,2],
        4:  [4,4,3],
        5:  [4,4,3,2],
        6:  [4,4,3,3],
        7:  [4,4,3,3,1],
        8:  [4,4,3,3,2],
        9:  [4,4,3,3,3,1],
        10: [5,4,3,3,3,2],
        11: [5,4,3,3,3,2,1],
        12: [5,4,3,3,3,2,1],
        13: [5,4,3,3,3,2,1,1],
        14: [5,4,3,3,3,2,1,1],
        15: [5,4,3,3,3,2,1,1,1],
        16: [5,4,3,3,3,2,1,1,1],
        17: [5,4,3,3,3,2,1,1,1,1],
        18: [5,4,3,3,3,3,1,1,1,1],
        19: [5,4,3,3,3,3,2,1,1,1],
        20: [5,4,3,3,3,3,2,2,1,1]
    }

    print("\nEnter wizard [level] [intelligence], optionally enter [school] preference")
    print("eg. 12 18 or evocation 12 18 for an 12th-level (evocation) wizard with 18 intelligence")

    while True:
        choice = input("\n> ").lower()
        choice_split = choice.split()

        level = 1
        int_score = 10
        school = ""

        if len(choice_split) == 2:
            level = int(choice_split[0])
            int_score = int(choice_split[1])
        elif len(choice_split) == 3:
            if choice_split[0] in ["abjuration", "conjuration", "divination", "enchantment", "evocation", "illusion", "necromancy", "transmutation"]:
                school = choice_split[0]
            level = int(choice_split[1])
            int_score = int(choice_split[2])

        int_mod = math.floor((int_score-10)/2)

        num_spells = level + int_mod
        if num_spells < 1:
            num_spells = 1

        if level > 20:
            level = 20
        elif level < 1:
            level = 1

        max_slot = len(spell_slots[level]) - 1

        prepared_by_slot = spell_slots[level]
        points_left = num_spells - sum(prepared_by_slot[1:])
        if points_left != 0:
            targets = []
            abs_points_left = abs(points_left)
            while abs_points_left > max_slot:
                targets.extend(random.sample(list(range(1, max_slot + 1)), max_slot))
                abs_points_left -= max_slot
            targets.extend(random.sample(list(range(1, max_slot + 1)), abs_points_left))
            for target in targets:
                if points_left > 0:
                    prepared_by_slot[target] += 1
                elif points_left < 0:
                    if prepared_by_slot[target] > 0:
                        prepared_by_slot[target] -= 1
        prepared_by_slot = [i for i in prepared_by_slot if i != 0]

        i = 0
        for prepare_num in prepared_by_slot:
            weights = gen_weights(spells, i, school)
            choices = gen_spells(prepare_num, spells, weights)
            choice_names = []
            for choice in choices:
                tag = ""
                if choice.get_school() == school:
                    tag = "*"
                choice_names.append(choice.get_name() + tag)
            if level >= 18:
                if i == 1 and choice_names:
                    mastery1 = choice_names[0]
                elif i == 2 and choice_names:
                    mastery2 = choice_names[0]
            choice_names = sorted(choice_names, key = str.casefold)
            print("{level}: ".format(level = i), end = "")
            print(", ".join(choice_names))
            i += 1
        
        if school:
            print("\n*{school} spell".format(school = school.capitalize()))
main()