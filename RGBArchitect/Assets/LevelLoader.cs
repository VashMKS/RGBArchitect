using UnityEngine;
using System.Collections;

[System.Serializable]
public class ColorToPrefab {
	public Color32 color;
	public GameObject prefab;
}

public class LevelLoader : MonoBehaviour {

	public string[] levelFileName;
	public string pack;
	public int currentLevel;

	private int numberOfLevels;

	public ColorToPrefab[] colorToPrefab;

	// Inicialization
	void Start () {
		// Constructor
		numberOfLevels = levelFileName.Length;
		LoadMap(currentLevel);
	}

	void EmptyMap() {
		// Find all of our children and... eliminate them.
		while(transform.childCount > 0) {
			Transform c = transform.GetChild(0);
			c.SetParent(null); // become Batman
			Destroy(c.gameObject); // become The Joker by killing the Batman
		}
	}

	// Loads the current level
	void LoadMap(int _level) {
		// clear the current level
		EmptyMap();
		// Debug.Log ("Welcome to level " + this.currentLevel);

		// Read the image data from the file in StreamingAssets
		string filePath = Application.dataPath + "/StreamingAssets/" + pack + "/" + levelFileName[_level];
		byte[] bytes = System.IO.File.ReadAllBytes(filePath);
		Texture2D levelMap = new Texture2D(2, 2);
		levelMap.LoadImage(bytes);


		// Get the raw pixels from the level imagemap into an array
		Color32[] allPixels = levelMap.GetPixels32();
		int width = levelMap.width;
		int height = levelMap.height;

		for (int x = 0; x < width; x++) {
			for (int y = 0; y < height; y++) {

				SpawnTileAt( allPixels[(y * width) + x], x, y );

			}
		}
	}

	void SpawnTileAt( Color32 c, int x, int y ) {

		// If this is a transparent pixel, then it's meant to just be empty.
		// Depending on our image processing we might want to ignore pure white pixels too
		if (c.a <= 0) 
			return;

		if (c == Color.white)
			return;

		// Find the right color in our color->prefab map

		// NOTE: This isn't optimized. You should have a dictionary lookup for max speed
		foreach(ColorToPrefab ctp in colorToPrefab) {
			
			if( c.Equals(ctp.color) ) {
				// Spawn the prefab at the right location
				GameObject go = (GameObject)Instantiate(ctp.prefab, new Vector3(x, y, 0), Quaternion.identity );
				go.transform.SetParent(this.transform);
				// maybe do more stuff to the gameobject here?
				return;
			}
		}

		// If we got to this point, it means we did not find a matching color in our array.

		Debug.LogError("No color to prefab found for: " + c.ToString() );

	}

	// Our end points send a message to call the end of a level
	public void EndCurrentLevel () {
		// load the next level (or the first one if it was the last) on the list
		currentLevel = (currentLevel + 1)%numberOfLevels;
		LoadMap(currentLevel);
	}
	
}
