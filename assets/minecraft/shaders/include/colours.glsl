#define T vec3(76., 64., 22.) // #4C4016 T for transparent

#define NO_SHADOW vec3(76., 69., 22.) // #4C4516

// Bars
#define BG_LEFT vec3(76., 64., 23.) // #4C4017
#define BG_RIGHT vec3(76., 64., 24.) // #4C4018

#define HEALTH vec3(76., 64., 25.) // #4C4019
#define STAMINA vec3(76., 64., 26.) // #4C401A
#define STAMINA_LOCKED vec3(76., 64., 27.) // #4C401B
#define SHIELD vec3(76., 64., 28.) // #4C401C
#define SHIELD_LOCKED vec3(76., 64., 36.) // #4C4024
#define AMMO vec3(76., 64., 37.) // #4C4025
#define AMMO_LOW vec3(76., 64., 38.) // #4C4026

#define CLOAK vec3(76., 64., 29.) // #4C401D
#define STRIKES vec3(76., 64., 30.) // #4C401E
#define MANA vec3(76., 64., 31.) // #4C401F
#define WARD vec3(76., 64., 40.) // #4C4028
#define CARDS vec3(76., 64., 32.) // #4C4020
#define DEVIL vec3(76., 64., 33.) // #4C4021
#define COLA vec3(76., 64., 34.) // #4C4022
#define SKELETON vec3(76., 64., 35.) // #4C4023
#define FREEZE vec3(76., 64., 39.) // #4C4027

#define TRANSITION_IN vec3(112., 102., 75.) // #70664B
#define TRANSITION_OUT vec3(112., 102., 76.) // #70664C

bool isColor(vec4 originColor, vec3 color) {
    return (originColor*255.).xyz == color;
}

vec4 getShadow(vec3 color) {
    return vec4(floor(color / 4.) / 255., 1);
}

vec4 getShadowAlt(vec3 color) {
    return vec4(ceil(color / 4.) / 255., 1);
}

bool isShadow(vec4 originColor, vec3 color) {
    return round(originColor.xyz*255.) == round(getShadow(color).xyz*255.) || round(originColor.xyz*255.) == round(getShadowAlt(color).xyz*255.);
}

bool isEither(vec4 originColor, vec3 color) {
    return isShadow(originColor, color) || isColor(originColor, color);
}

vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}