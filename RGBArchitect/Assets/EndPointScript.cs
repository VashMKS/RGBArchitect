using UnityEngine;
using System.Collections;

public class EndPointScript : MonoBehaviour {

	void OnTriggerEnter2D(Collider2D other) {
		Debug.Log ("auch!");
		// as soon as a player hits the end of a level it ends
		if (other.gameObject.tag == "Player") {
			LevelLoader ownLevel = GameObject.Find("Level").GetComponent<LevelLoader>();
			ownLevel.EndCurrentLevel ();
		}
	}

}
