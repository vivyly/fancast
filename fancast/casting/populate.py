#/usr/bin/env python
from .models import Character, Project, Actor, Prospect
from fancast.lib.name import normalize

BEBOP = {"Spike Spiegel" : dict(image =  """http://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Spike_Spiegel_as_drawn_by_the_creators.jpg/230px-Spike_Spiegel_as_drawn_by_the_creators.jpg""",
                           desc="""Spike is a fictional bounty hunter who was born on Mars, June 26, 2044. According to the anime guides, he is 27 years old and has fluffy dark-green hair [3] and brown eyes; one of which is artificial and lighter than the other. His right eye was surgically replaced with a cybernetic one. He is usually dressed in a blue leisure suit, with a yellow shirt and boots similar to those worn by Arsene Lupin III. Spike often smokes cigarettes, despite rain or "no smoking" signs. He stands 6'1" and weighs 155 lbs.""",
                           order=0),
        "Faye Valentine" : dict(image="""http://images1.wikia.nocookie.net/__cb20090726171256/cowboybebop/images/5/5b/Faye_tall.jpg""",
                                desc="""One of the members of the bounty hunting crew in the anime series Cowboy Bebop. Often seen with a cigarette and in a revealing outfit complete with bright yellow hot pants and a matching, revealing top, black suspenders, white boots, and a long-sleeved red shirt worn normally through the sleeves, not to mention her signature headband, she is unusually attractive, sporting a bob of violet hair, green eyes, fair skin, and a voluptuous body. Although appearing to be no more than her 23 years alive suggests, Faye is actually upwards of 74-years-old, having been put into cryogenic freeze after a space shuttle accident. During the course of the series (set in 2071), Faye manages to cross paths with Spike and Jet twice before she finally makes herself at home aboard their ship the second time, much to the consternation and disapproval of the two men, both of whom have their own reservations about women in general. Faye herself is brash, egotistical, and quite lazy, despite taking plenty of time to pamper and care for her own appearance. Faye has also been placed under arrest several times in the series and spends much time in handcuffs on the ship. She, at times, expects the boys to take care of bounties for her, while she sits by idly to reap the benefits and eat all their food, another source of conflict.""",
                                order=2),
        "Jet Black" : dict(image="""http://amazingstoriesmag.com/wp-content/uploads/2013/07/jet-black.png""",
                           desc="""Born December 4, 2035, and known on his home satellite as the "Black Dog" for his tenacity, Jet Black is a 36-year-old former cop from Ganymede (a Jovian satellite) and acts as Spike's foil during the series. Physically, Jet is very tall with a muscular build. He wears a beard with no mustache, and is completely bald save for the back of his head. Spike acts lazy and uninterested, whereas Jet is hard working and a jack-of-all-trades.""",
                           order=1),
        "Edward" : dict(image="""http://images1.wikia.nocookie.net/__cb20090406042714/cowboybebop/images/9/9d/9_EdFlyBebop2.png""",
                        desc="""Edward Wong Hau Pepelu Tivruski IV, born January 1, 2058) is the self-invented personal name of an elite hacker prodigy from Earth. Her birth name is Francoise Appledehli. "Radical Edward" is a very strange, somewhat androgynous, teenage girl claiming to be around 13 years of age. Her mannerisms include walking around in her bare feet, performing strange postures, and her gangling walk. Ed could be considered a "free spirit;" she is fond of silly exclamations and childish rhymes, is easily distracted, has the habit of "drifting off" from reality...sometimes in mid-sentence, and is the show's primary source of physical humor. Ed's generally carefree attitude and energy act as a counterpoint to the more solemn and dark aspects of the show.""",
                        order=4),
        "Ein" : dict(image="""http://www.overthinkingit.com/wp-content/uploads/2009/11/ein03.jpg""",
                     desc="""Ein is a Pembroke Welsh Corgi brought aboard the Bebop by Spike after a failed attempt to capture a bounty. His name is most likely derived from "Einstein", after Albert Einstein, because of the extraordinary intelligence he possesses. Ein is referred to as a "data dog" by the scientists that created him and he often shows heightened awareness of events going on around him. Over the course of the series, Ein answers the telephone, steers a car, uses the SSW, plays shogi, and generally performs tasks that an average canine should not be able to accomplish. The extent of Ein's intelligence is hinted at in Session 23: "Brain Scratch" when the "Brain Dream" gaming device is placed on Ein's head; Ein quickly navigates the system and hacks into its operating system.""",
                     order=5),
        "Vicious" : dict(image="""http://www.otakuvillage.com/images/D/cowboy_bebop_Vicious_costume_ver_01-3-05.jpg""",
                         desc="""Vicious is ruthless, bloodthirsty, cunning and ambitious. Considered by some to be Spike's darker half, Vicious is willing to do anything in order to secure a position of power. He is a member of the Red Dragon Crime Syndicate in Tharsis, and is often referred to or depicted as a venomous snake (as opposed to Spike who is referred to as a swimming bird and the Syndicate Elders who see themselves as a dragon). His weapon of choice is not a firearm, but a katana which he wields skillfully, even against gun-wielders. He was an infantry rifleman during the Titan War and is shown firing a semi-automatic pistol in a Session 5 flashback, as well as in the Session 26 flashback of him and Spike fighting back-to-back. Early on, Vicious is seen with a black bird on his shoulder""",
                         order=6),
        "Julia" : dict(image="""http://images2.wikia.nocookie.net/__cb20090316022730/cowboybebop/images/7/71/5_Julia2.png""",
                       desc="""Julia is a beautiful and mysterious woman from both Spike and Vicious' pasts. Initially Vicious' girlfriend and a Syndicate member herself, she and Spike started a dangerous affair that led to Spike offering to abandon the Syndicate and elope with her, despite the fact that the Syndicate punishes desertion with death. Arranging to meet at a graveyard later, Spike goes to confront the Syndicate with his resignation, resulting in a violent gun battle where he is presumed by the Syndicate to have died.""",
                       order=7),
        }


ACTOR = {'Joseph Gordon Levitt': dict(character="Spike Spiegel",
                                      image = "http://mediacdn.disqus.com/uploads/mediaembed/images/353/7032/original.jpg",
                                      desc = "Batman, Looper",
                                      upvotes = 6,
                                      downvotes = 0),
         'Ben Schwartz': dict(character="Spike Spiegel",
                              image = "http://images1.wikia.nocookie.net/__cb20130405031244/randycunningham9thgradeninja/images/a/a7/Ben_Schwartz.jpg",
                              desc = "comedian",
                              upvotes = 1,
                              downvotes = 5),
         "Keanu Reeves": dict(character="Spike Spiegel",
                              image = "http://images.icnetwork.co.uk/upl/liverpoolecho/may2013/1/9/image-2-for-world-in-pictures-may-3-2013-gallery-147523457.jpg",
                              desc = "Matrix",
                              upvotes = 2,
                              downvotes = 4),
         "Adrien Brody": dict(character="Spike Spiegel",
                              image = "http://www.swingfashionista.com/wp-content/uploads/2010/05/adrien-brody.jpg",
                              desc = "Brothers Bloom",
                              upvotes = 3,
                              downvotes = 2),
         "Lee Pace": dict(character="Spike Spiegel",
                          image = "http://img.poptower.com/pic-48967/lee-pace.jpg?d=1024",
                          desc = "The Fall, The Hobbit, Twilight",
                          upvotes = 3,
                          downvotes = 3),
         "Byung Hun Lee": dict(character = "Spike Spiegel",
                               image = "http://tong.visitkorea.or.kr/cms/resource_etc/19/808519_image2_1.jpg",
                               desc = "Storm Shadow",
                               upvotes = 4,
                               downvotes = 2
                            ),
         'Ron Perlman': dict(character="Jet Black",
                             image = "http://media.zenfs.com/en_us/tv_show/TV/ron-perlman-50373.jpg",
                             desc = "Hellboy",
                             upvotes = 7,
                             downvotes = 1),
         "Olivia Wilde": dict(character="Faye Valentine",
                              image = "http://www.beyondhollywood.com/uploads/2010/04/olivia-wilde-tron-legacy-2.jpg",
                              desc = "Tron",
                              upvotes = 6,
                              downvotes = 2),
         "Eva Green": dict(character="Faye Valentine",
                           image = "http://4.bp.blogspot.com/-1aNLqsGTzzc/UJ949Po86mI/AAAAAAAAESc/Zm716mwnpPw/s400/Vesper-Lynd-Casino-Royale-2006.jpg",
                           desc = "Bond, Femme Fatale",
                           upvotes = 5,
                           downvotes = 1),
         "Maisie Williams": dict(character="Edward",
                              image = "http://mywalkoffame.files.wordpress.com/2012/11/maisie-williams-got-itacon-2013.jpg?w=549",
                              desc = "Game of Thrones",
                              upvotes = 7,
                              downvotes = 0),
         "Jasper Islington": dict(character="Ein",
                        image = "http://25.media.tumblr.com/e0f24ccba3b380cc5c19378b6a1a24b9/tumblr_mu9q45Xdb21rbbodpo1_500.jpg",
                        desc = "cutest dog evar",
                        upvotes = 10,
                        downvotes = 1),
         "Benedict Cumberbatch": dict(character="Vicious",
                                      image = "http://i.dailymail.co.uk/i/pix/2013/07/17/article-2366612-1AD9C4C6000005DC-403_634x478.jpg",
                                      desc = "Sherlock, Fifth Estate",
                                      upvotes = 15,
                                      downvotes = 5),
         "Michael Fassbender": dict(character="Vicious",
                                    image = "http://metrouk2.files.wordpress.com/2012/05/article-1338472590434-135aa916000005dc-997629_465x348.jpg",
                                    desc = "Xmen",
                                    upvotes = 9,
                                    downvotes = 2),
         "Ryan Gosling": dict(character = "Vicious",
                              image = "http://img2.timeinc.net/people/i/2012/specials/sag/nominees/ryan-gosling-435.jpg",
                              desc = "Drive",
                              upvotes = 5,
                              downvotes = 3),
         "Diane Kruger": dict(character="Julia",
                              image = "http://4.bp.blogspot.com/-17UaFGUg9e8/UORUHeyvI0I/AAAAAAAAAU8/fG1_Q9KHcvc/s1600/Diane+Kruger+6.jpg",
                              desc = "generic blonde",
                              upvotes = 3,
                              downvotes = 0),
         "Jenny Wade": dict(character="Julia",
                            image = "http://www.sitcomsonline.com/photopost/data/3462/wedding-band-jenny-wade-1.jpg",
                            desc = "other generic blonde",
                            upvotes = 0,
                            downvotes = 0),

}

def create_project():
    proj = Project()
    proj.origin = 'anime'
    proj.derivation = 'movie'
    proj.origin_title = 'Cowboy Bebop'
    proj.derived_title = 'Cowboys in Space'
    proj.save()
    return proj

def create_character(name, image, description, order, project):
    chrt = Character()
    chrt.name = name
    chrt.normalized = normalize(name)
    chrt.image = image
    chrt.description = description
    chrt.project = project
    chrt.order = order
    chrt.save()
    return chrt

def create_bebop(project):
    for name, data in BEBOP.iteritems():
        create_character(name,
                         data.get('image'),
                         data.get('desc'),
                         data.get('order'),
                         project)

def create_actor(name, image, description):
    actor = Actor()
    actor.name = name
    actor.normalized = normalize(name)
    actor.image = image
    actor.description = description
    actor.save()
    return actor


def create_relation(actor, character_name):
    character = Character.objects.get(normalized=normalize(character_name))
    prospect = Prospect()
    prospect.actor = actor
    prospect.character = character
    prospect.save()


def bebop_potential_actors():
    actors = []
    for name, data in ACTOR.iteritems():
        actor = create_actor(name, data.get('image'), data.get('desc'))
        create_relation(actor, data.get('character'))
        actors.append(actor)
    return actors


def main():
    project = create_project()
    create_bebop(project)
    bebop_potential_actors()

if __name__ == "__main__":
    main()
